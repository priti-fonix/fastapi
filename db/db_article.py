
from db.models import DbArticle
from schema import ArticleBase
from sqlalchemy.orm.session import Session
from sqlalchemy.orm import joinedload
from fastapi import HTTPException, status


def create_article(db: Session, request: ArticleBase):
    new_article = DbArticle(
        title=request.title,
        content=request.content,
        published=request.published,
        user_id=request.creator_id
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    # Ensure user relationship is loaded
    if not new_article.user:
        new_article.user = db.query(DbArticle).filter(DbArticle.id == new_article.id).first().user
    return new_article

def get_article(db: Session, id: int):
    article = db.query(DbArticle).options(joinedload(DbArticle.user)).filter(DbArticle.id == id).first()
    if not article or not article.user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Article or user not found")
    return article