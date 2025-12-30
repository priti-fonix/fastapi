from fastapi import APIRouter, File, UploadFile
import shutil


router = APIRouter(
    prefix='/file',
    tags=['file']
)

@router.post('/file')
def post_file(file: bytes= File(...)):
  content = file.decode('utf-8')
  lines = content.split('\n')
  return {'lines': lines}

@router.post('/uploadfile')
def get_uploadfile(upload_file: UploadFile= File(...)):
#   content = UploadFile.decode('utf-8')
#   lines = content.split('\n')
    path = f"files/{upload_file.filename}"
    with open(path,'w+b') as buffer:
        shutil.copyfileobj(upload_file.file,buffer)
     
        
    return {
      'filename': path,
      "type": upload_file.content_type
      }
