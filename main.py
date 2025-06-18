import base64
from fastapi import FastAPI
from pydantic import BaseModel
from services.compress import compress

app = FastAPI()

class Items(BaseModel):
    data : object
    output_name: str

@app.post("/compress_pdf_tla")
def main_funct(item: Items):
    data = item.data
    try: 
        for key, value in data.items():
            if value != "application/pdf" and value != "application/octet-stream":
                bynary_data = base64.b64decode(value)
                save_path = fr"C:/Users/simon/OneDrive/Documents/Simon/Compress_Files/{item.output_name}.pdf"

                with open(save_path, "wb") as file:
                    file.write(bynary_data)

                compress(save_path, fr"C:/Users/simon/OneDrive/Documents/Simon/Compress_Files/{item.output_name}2.pdf")

                return {"message": "Archivo PDF recibido y guardado correctamente", "path": save_path}
    except Exception as e:
        return {"error": str(e)}