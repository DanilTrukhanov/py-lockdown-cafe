import datetime

from app.errors import NotWearingMaskError
from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("You are not vaccinated!")

        today = datetime.date.today()
        if today > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError("Your vaccine is outdated!")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("You are not wearing a mask!")

        return f"Welcome to {self.name}"
