
from fastapi import HTTPException, Header
from dependency_injector.wiring import inject
import jwt


@inject
async def verify_token(x_token: str = Header(...)):
    try: 
        data = jwt.decode(x_token, "secret_config", algorithms=["HS256"])
        return data  
    except Exception as ex:
        raise HTTPException(status_code=401, detail=str(ex))



