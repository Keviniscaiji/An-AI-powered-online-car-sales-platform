from app.models import *
from ._dev_data import *
import datetime


def insert_roles():
    for item in ROLES:
        role = Role(name=item["name"])
        db.session.add(role)
    db.session.commit()


def insert_categories():
    objs = []
    for item in CATEGORIES:
        category = Category(name=item["name"])
        db.session.add(category)
        objs.append(category)
    db.session.commit()
    return objs


def insert_users():
    for item in USERS:
        user = User(
            email=item["email"], username=item['username'], role_id=item['role_id'],
            password_hash=generate_password_hash(item['password']), confirmed=item["confirmed"],
            avatar_path=item["avatar_path"]
        )
        db.session.add(user)
    db.session.commit()


def insert_products(cat_objs):
    for item, category in zip(PRODUCTS, PRODUCTS2CATEGORIES):
        product = Product(
            key=item['key'], name=item['name'], brand=item['brand'], model=item['model'], year=item['year'],
            max_speed=item['max_speed'], oil_consumption=item['oil_consumption'], price=item['price'],
            description=item['description']
        )
        for j in category['category_ids']:
            product.categories.append(cat_objs[j-1])
        db.session.add(product)
    db.session.commit()


def insert_custproducts(cat_objs):
    for item, category in zip(CUSTPRODUCTS, PRODUCTS2CATEGORIES):
        product = Product(
            key=item['key'], name=item['name'], brand=item['brand'], model=item['model'], year=item['year'],
            max_speed=item['max_speed'], oil_consumption=item['oil_consumption'], price=item['price'],
            description=item['description'], is_hidden=item['is_hidden']
        )
        for j in category['category_ids']:
            product.categories.append(cat_objs[j-1])
        db.session.add(product)
    db.session.commit()


def insert_product_orders():
    for item in PRODUCTORDERS:
        productOrder = ProductOrder(customized_color=item['customized_color'], count=item['count'],
                                    product_id=item['product_id'], order_id=item['order_id'])
        db.session.add(productOrder)
    db.session.commit()


def insert_orders():
    for item in ORDERS:
        order = Order(timestamp=item['timestamp'], pick_up_time=item['pick_up_time'], note=item['note'],
                      status=item['status'], price=item['price'], priority=item['priority'], buyer_id=item['buyer_id'])
        db.session.add(order)
        db.session.commit()
        order_aim = Order.query.filter_by(buyer_id=item['buyer_id']).first()
        productOrder_list = ProductOrder.query.filter_by(order_id=order_aim.id).all()
        for po in productOrder_list:
            order_aim.productOrders.append(po)
        db.session.commit()


def insert_drives():
    for item in DRIVES:
        drive = Drive(timestamp=item['timestamp'], drive_time_start=item['drive_time_start'],
                      drive_time_end=item['drive_time_end'], note=item['note'], status=item['status'],
                      priority=item['priority'], buyer_id=item['buyer_id'])
        db.session.add(drive)
        db.session.commit()


def insert_views():
    for item in VIEWS:
        view = View(timestamp=item['timestamp'], buyer_id=item['buyer_id'])
        db.session.add(view)
        db.session.commit()


def insert_carts():
    for item in CARTS:
        cart = Cart(count=item["count"], customized_color=item['customized_color'], owner_id=item['owner_id'],
                    product_id=item['product_id'], is_selected=item['is_selected'])
        db.session.add(cart)
    db.session.commit()


def insert_product_image_paths():
    for item in PRODUCTIMAGEPATHS:
        productImagePath = ProductImagePath(
            image_path=item['image_path'], resized_image_path=item['resized_image_path'], product_id=item['product_id']
        )
        db.session.add(productImagePath)
    db.session.commit()


def insert_blogs():
    for item in BLOGS:
        blogs = Blog(
            id=item['id'], title=item['title'], content=item['content'], author_id=item['author_id']
        )
        db.session.add(blogs)
    db.session.commit()


def insert_blog_image_paths():
    for item in BLOGIMAGEPATHS:
        blogImagePath = BlogImagePath(
            image_path=item['image_path'], blog_id=item['blog_id']
        )
        db.session.add(blogImagePath)
    db.session.commit()


def insert_blog_comments():
    for item in BLOGCOMMENTS:
        blogComments = BlogComment(
            body=item['body'], blog_id=item['blog_id'], author_id=item['author_id']
        )
        db.session.add(blogComments)
    db.session.commit()


def reset():
    # Drop and create
    db.drop_all()
    db.create_all()


def insert_all():
    db.session.execute("SET FOREIGN_KEY_CHECKS=0;")
    # Insert Role
    insert_roles()
    # Insert Category
    cat_objs = insert_categories()
    # Insert User
    insert_users()
    # Insert Products
    insert_products(cat_objs)
    insert_custproducts(cat_objs)
    # Insert Carts
    insert_carts()
    # Insert ProductImagePaths()
    insert_product_image_paths()
    # Insert Blogs
    insert_blogs()
    # Insert BlogImagePaths
    insert_blog_image_paths()
    # Insert BlogComments
    insert_blog_comments()

    insert_product_orders()

    insert_orders()

    insert_drives()

    insert_views()

