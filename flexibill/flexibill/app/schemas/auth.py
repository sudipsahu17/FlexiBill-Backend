from pydantic import BaseModel, Field, ConfigDict


class OTPSendRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        allow_population_by_alias=True
    )
    mobile_number: str = Field(..., example="9876543210", alias="mobileNumber")


class OTPVerifyRequest(OTPSendRequest):
    otp: str = Field(..., example="123456")
