import pytesseract
from PIL import Image, ImageOps
import re
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from .models import ScannedReceipt

class OCRView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        # Obtener la imagen del request
        image = request.FILES.get('image')
        if not image:
            return Response({"error": "No image provided."}, status=400)

        # Preprocesar la imagen para mejorar el OCR
        try:
            img = Image.open(image).convert('L')  # Convertir a escala de grises
            img = ImageOps.autocontrast(img)  # Ajustar contraste
        except Exception as e:
            return Response({"error": "Error processing image.", "details": str(e)}, status=400)

        # Procesar la imagen con Tesseract OCR
        try:
            text = pytesseract.image_to_string(img)
        except pytesseract.TesseractNotFoundError:
            return Response({"error": "Tesseract is not installed or not in PATH."}, status=500)
        except Exception as e:
            return Response({"error": "Error during OCR processing.", "details": str(e)}, status=500)

        # Mostrar el texto extraído en los logs (para depuración)
        print("Texto extraído por OCR:", text)

        # Extraer datos relevantes del texto
        try:
            lines = text.splitlines()
            store_name = lines[0] if lines else "Unknown Store"

            # Buscar el monto total usando una expresión regular ajustada
            print("Texto preprocesado para regex:", text.replace(',', '.'))  # Log adicional
            total_match = re.search(r'(TOTAL|Total|total)\s*[:\s]*([\d]+[.,]\d{2})', text.replace(',', '.'), re.IGNORECASE)

            # Depurar el resultado de la expresión regular
            if total_match:
                print("Resultado de la expresión regular:", total_match.group(2))
                total = float(total_match.group(2))
            else:
                print("No se encontró un monto en el texto.")
                total = None
        except Exception as e:
            return Response({"error": "Error extracting data from text.", "details": str(e)}, status=400)

        # Validar si no se encontró el total
        if total is None or not isinstance(total, float):
            return Response({
                "error": "Could not extract a valid amount from the ticket.",
                "raw_text": text
            }, status=400)

        # Guardar el registro en la base de datos
        try:
            receipt = ScannedReceipt.objects.create(
                user=request.user,
                store_name=store_name,
                total=total,
                image=image
            )
        except Exception as e:
            return Response({"error": "Error saving to database.", "details": str(e)}, status=500)

        # Responder con los datos extraídos
        return Response({
            "store_name": receipt.store_name,
            "total": receipt.total,
            "raw_text": text
        })
