import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone: str
    subject: str
    current_address: str
    state: str
    city: str
    day_birth: str
    month_birth: str
    year_birth: str
    photo: str
    hobbies: str


admin = User(
    first_name="Test",
    last_name="Testov",
    email="Testov@test.com",
    gender="Male",
    phone="9628082744",
    subject="Maths",
    current_address="Testova str, 8, apt.10",
    state="NCR",
    city="Delhi",
    day_birth="01",
    month_birth="January",
    year_birth="1991",
    photo="meme.png",
    hobbies="Sports, Music",
)
