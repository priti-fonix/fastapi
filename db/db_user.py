from sqlalchemy.orm.session import Session
from schema import UserBase
from db.models import Dbuser
from db.hash import Hash
from fastapi import HTTPException, status,Depends

def create_user(db:Session, request: UserBase):
    hash_pass = Hash.create(request.password)
    new_user = Dbuser(username =  request.username,
                      email = request.email,
                      password = hash_pass
                      )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all_users(db:Session):
    return db.query(Dbuser).all()

def get_user_by_username(db:Session,username: str):
    user = db.query(Dbuser).filter(Dbuser.username == username).first()
    
    if not user: 
        raise HTTPException(status_code=status.HTTP_404, detail=f"user details with {username} not found")
    return user

def update_user(db:Session, id: int, request:UserBase):
    user = db.query(Dbuser).filter(Dbuser.id == id)
    user.update({
        Dbuser.username: request.username,
        Dbuser.email: request.email,
        Dbuser.password: Hash.create(request.password)
    })
    db.commit()
    return user.first()


def delete_user(db:Session, id: int):
    user = db.query(Dbuser).filter(Dbuser.id == id).first()
    if not user:
        
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return user



'''
sess.query(User).filter(User.age == 25).update(
        {User.age: User.age - 10}, synchronize_session=False
    )
    '''