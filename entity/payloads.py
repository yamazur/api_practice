from faker import Faker

fake = Faker()

class Payload:

    @staticmethod
    def create_entity():
        return {
        "addition": {
            "additional_info": fake.text(),
            "additional_number": fake.random_int(),
        },
        "important_numbers": fake.random_elements(
            elements=range(1, 100),
            length=3,
            unique=True
        ),
        "title": fake.sentence(),
        "verified": True
    }

    @staticmethod
    def update_entity():
        return {
        "addition": {
            "additional_info": fake.text(),
            "additional_number": fake.random_int(),
        },
        "important_numbers": fake.random_elements(
            elements=range(1, 100),
            length=3,
            unique=True
        ),
        "title": fake.sentence(),
        "verified": True
    }
