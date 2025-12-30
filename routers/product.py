from fastapi import APIRouter, Form, Header,Cookie
from fastapi.responses import Response,HTMLResponse
from typing import Optional, List,Tuple, Dict


router = APIRouter( 
    prefix= '/products',
    tags=['products']
)

products =["watch","magazines","phones"]

@router.post('/new')
def create_product(name:str=Form(...)):
    products.append(name)
    return products

#-------------- cookie- setting -------//
@router.get('/all')
def get_all_products():
    data = " ".join(products)
    response = Response(content=data, media_type="text/plain")
    response.set_cookie(key='test_Cookie', value="text_cookie_value")
    
    return response

@router.get('/withheader')
def get_all_products(
    response: Response,
    custom_header: Optional[List[str]] = Header(None),
    test_cookie: Optional[str] = Cookie(None)
):
    if custom_header:
    # data = " ,".join(products)
      response.headers["custom-response-header"] = "and" .join(custom_header)
    return{
        "data": products,
        "custom_header" : custom_header,
        "my_cookie":test_cookie
        }
    
    # if custom_header:
    #     if isinstance(custom_header, list):
    #         response.headers["custom-response-header"] = custom_header[0]
    #     else:
    #         response.headers["custom-response-header"] = custom_header
    # return Response(content=data, media_type="text/plain")
    
    
@router.get('/{id}',responses={
    # customizing the responses 
    200:{
        "content":{
            "text/plain":{
                "example": "<div> Product</div>"
            }
        },
        "description": "returns the html response for an object"
    },
    404:{
        "content":{
            "text/plain":{
                "Products are not available"
            }
        },
        "description": "A cleartext error message"
    }
})
def get_product(id:int):
        if 0 <= id < len(products):
                product = products[id]
                out = f"""
                <head>
                    <style>
                    .product{{
                            width: 500px;
                            height: 30px;
                    }}
                    </style>
                </head>
                <div class="product">{product}</div>
                """
                return HTMLResponse(content=out, media_type="text/html")
        return Response(content="Products are not available", media_type="text/plain", status_code=404)
    
    # '''
    # @router.get('/withheader)
    # def get_all products( custom_header: Optional[str] = Header(None))
    
    
    
    # '''