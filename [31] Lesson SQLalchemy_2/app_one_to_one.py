from sqlalchemy.orm import sessionmaker
from models import engine, Profile, User

Session = sessionmaker(bind=engine)
session = Session()


# insert data

user1 = User(userName="Dato", email="dato@gmail.com")
user2 = User(userName="Nika", email="nika@gmail.com")
user3 = User(userName="Ana", email="ana@yahoo.com")

profile1 = Profile(bio="very good boy...", profilePicture="img/u_00001.jpg", user=user1)
profile2 = Profile(bio="good boy...", profilePicture="img1/u_00002.jpg", user=user2)
profile3 = Profile(bio="living in England...", profilePicture="img/u_00003.jpg", user=user3)

# session.add_all([user1, user2, user3, profile1, profile2, profile3])




# --------------------------

# session.commit()



# read data

# users = session.query(User).all()
# for user in users:
#     print(user.id, user.userName, user.email, user.profile.bio, user.profile.profilePicture)


user = session.query(User).filter_by(userName="dato").first()
if user is not None:
    print(user.id, user.userName, user.email, user.profile.bio, user.profile.profilePicture)
