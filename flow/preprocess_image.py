import requests
from PIL import Image
from promptflow.contracts.multimedia import Image as PFImage
import io
from io import BytesIO
from promptflow.core import tool

@tool
def load_image_from_url(url: str) -> PFImage:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        image = Image.open(BytesIO(response.content))
        
        byte_arr = io.BytesIO()
        image.save(byte_arr, format="JPEG")
        
        return PFImage(byte_arr.getvalue(), mime_type="image/jpeg")
    
    except Exception as e:
        raise RuntimeError(f"圖片載入失敗: {e}")
