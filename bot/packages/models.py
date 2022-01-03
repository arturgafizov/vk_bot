from sqlalchemy import Column, DateTime, String, Integer, func, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
# from sqlalchemy_imageattach.entity import Image, image_attachment
from .database import Base


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    category = relationship("category", back_populates="product")
    # image = image_attachment('ProductImage')
    description = Column(String)


product = Product.__table__


# class ProductImage (Base, Image):
#     __tablename__ = 'Product_image'
#     product_id = Column(Integer, ForeignKey('product.id'), primary_key=True)
#     product = relationship('Product')
#
#
# product_image = ProductImage.__table__


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    category = Column(String)
    product_id = Column(Integer, ForeignKey('product.id'))
    product = relationship("product", back_populates="category")


category = Category.__table__
