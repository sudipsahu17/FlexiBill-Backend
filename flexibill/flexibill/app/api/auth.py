import logging

from app.schemas.auth import OTPSendRequest, OTPVerifyRequest
from app.schemas.base import BaseResponse
from app.utils.auth import create_access_token
from fastapi import APIRouter, HTTPException

logger = logging.getLogger(__name__)
auth_router = APIRouter(prefix="/auth", tags=["auth"])

MOBOLE_NUMBER_OTP_MAP = {}


@auth_router.post("/send-otp")
async def send_otp(request: OTPSendRequest) -> BaseResponse:
    # Dummy verification logic, replace with actual implementation
    MOBOLE_NUMBER_OTP_MAP[request.mobile_number] = "123456"
    if MOBOLE_NUMBER_OTP_MAP.get(request.mobile_number):
        return BaseResponse(message="OTP created successfully")
    else:
        raise HTTPException(status_code=400, detail="Invalid OTP or mobile number")


@auth_router.post("/verify-otp")
async def verify_otp(request: OTPVerifyRequest) -> BaseResponse:
    logger.debug(f"Mobile number: {request.mobile_number} and OTP: {request.otp}")
    if MOBOLE_NUMBER_OTP_MAP.get(request.mobile_number) == request.otp:
        token = create_access_token({"mobile_number": request.mobile_number})
        return BaseResponse(
            message="OTP verified successfully",
            data={
                "mobile_number": request.mobile_number,
                "access_token": token,
                "token_type": "bearer",
            },
        )
    else:
        raise HTTPException(status_code=400, detail="Invalid OTP or mobile number")
