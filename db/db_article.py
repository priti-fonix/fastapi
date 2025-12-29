from db.models import DbArticle
from schema import ArticleBase
from sqlalchemy.orm.session import Session
from sqlalchemy.orm import joinedload
from fastapi import HTTPException, status
from exceptions import storyException


def create_article(db: Session, request: ArticleBase):
    if request.content.lower().startswith('once upon a time'):
        raise storyException('No stories please')
    
    new_article = DbArticle(
        title=request.title,
        content=request.content,
        published=request.published,
        user_id=request.creator_id
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    # Reload with user relationship
    article_with_user = db.query(DbArticle).options(joinedload(DbArticle.user)).filter(DbArticle.id == new_article.id).first()
    return article_with_user

def get_article(db: Session, id: int):
    article = db.query(DbArticle).options(joinedload(DbArticle.user)).filter(DbArticle.id == id).first()
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Article not found")
    return article