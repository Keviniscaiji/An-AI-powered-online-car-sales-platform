import datetime
import random
import os
from flask import render_template, request, jsonify, current_app, session, redirect, url_for, flash

from flask import render_template, request, jsonify, current_app, redirect, url_for, session
from flask_login import login_required, current_user
from sqlalchemy import desc, case

import app
from app import db, babel
from app.models import Product, ProductImagePath, Cart, User, Category, Comment, Order, ProductOrder, Blog, BlogComment, \
    BlogImagePath, Drive, ProductDrive
from config import Config
from werkzeug.utils import secure_filename
from . import main
from .forms import CommentForm

# IR start
import pickle
import calendar
from openvino.runtime import Core

from app.ir.ir_with_hci import *
from app.ir.configs.ml_config import *
from app.ir.configs.flask_config import *

## Load Models and Index
# Load RTMDet-Ins
engine = RTMDetInsEngine()
print("RTMDet-Ins Model Loaded")

# Load Encoder
# ie3 = Core()
# net3 = ie3.read_model(ir_cfg['encoder_path'])
# compiled_model3 = ie3.compile_model(net3, 'CPU')
import onnxruntime as rt
sess = rt.InferenceSession(ir_cfg['encoder_path'])
print("ResNet50Encoder Model Loaded")

# Load Index
with open(ir_cfg['index_path'], "rb") as f:
    ir_index = pickle.load(f)
# IR end


@babel.localeselector
def get_locale():
    # return request.accept_languages.best_match(app.config['LANGUAGES'])
    if session.get("language") is not None:
        # print(session['language'])
        if session['language'] == 'Chinese':
            return 'zh'
    return 'en'


@main.route('/change_language', methods=['POST', 'GET'])
def change_language():
    if request.method == 'POST':
        if request.values['language'] == 'Chinese':
            session['language'] = 'Chinese'
            session['alternative_language'] = 'English'
        else:
            session['language'] = 'English'
            session['alternative_language'] = 'Chinese'
    return session['language']


@main.route('/', methods=['POST', 'GET'])
def index():
    """
    View function for home page
    """
    # --- Display definition ---
    n_max_col = 6
    n_max_row_pc = 2
    n_max_row_pa = 1
    n_max_row_pbs = 2

    n_max_row = max(n_max_row_pa, n_max_row_pc, n_max_row_pbs)
    # --------------------------

    products_collection = []
    products_area = []  # pa
    products_countdown = []  # pc
    products_best_seller = []  # pbs

    products_all = Product.query.all()
    n_products = len(products_all)

    if n_products > n_max_row * n_max_col:
        random.shuffle(products_all)

    if 0 < n_products <= 1:
        products_collection += [products_all[0], products_all[0]]
        products_area.append([products_all[0]])
        products_countdown.append([products_all[0]])
        products_best_seller.append([products_all[0]])
    elif 2 <= n_products <= n_max_col:
        products_collection += [products_all[0], products_all[1]]
        for i, item in enumerate(products_all):
            if i >= n_max_row * n_max_col:
                break
            products_area.append([item])
            products_countdown.append([item])
            products_best_seller.append([item])

    elif n_products > n_max_col:
        products_collection += [products_all[0], products_all[1]]
        products_area = [[] for _ in range(n_max_col)]
        products_countdown = [[] for _ in range(n_max_col)]
        products_best_seller = [[] for _ in range(n_max_col)]
        for i, item in enumerate(products_all):
            if i >= n_max_row * n_max_col:
                break
            if i < n_max_col * n_max_row_pc:
                products_area[i % n_max_col].append(item)
            if i < n_max_col * n_max_row_pa:
                products_countdown[i % n_max_col].append(item)
            if i < n_max_col * n_max_row_pbs:
                products_best_seller[i % n_max_col].append(item)
    else:
        pass

    return render_template(
        'index-3.html',
        products_collection=products_collection,
        products_area=products_area,
        products_countdown=products_countdown,
        products_best_seller=products_best_seller)


def check_is_ir_search(ir):
    if len(ir.split("_")) != 3:
        return False
    if ir[:3] != "irs":
        return False
    if len(ir.split("_")[1]) != 10:
        return False
    return True


@main.route('/products/<string:status>', methods=['POST', 'GET'])
def shop(status):
    categories = Category.query.all()
    cate_num = []
    for c in categories:
        num = len(list(c.products))
        cate_num.append(num)
    page = request.args.get('page', 1, type=int)

    if status == "init":
        search, cate, low, high, sort, ir = "non", "all", "non", "non", "non", "non"
    elif status == "search":
        search, cate, low, high, sort, ir = request.form.get("searchcontent"), "all", "non", "non", "non", "non"
    elif status == "filtrate":
        search = request.form.get("searchselect")
        cate = request.form.get("cateselect")
        low = splitlow(request.form.get("priceselect"))
        high = splithigh(request.form.get("priceselect"))
        sort = request.form.get("sortselect")
        ir = request.form.get("irselect")
        if search is None:
            search = session.get("search")
        if cate is None:
            cate = session.get("cate")
        if low is None:
            low = session.get("low")
        if high is None:
            high = session.get("high")
        if sort is None:
            sort = session.get("sort")
        if ir is None:
            ir = session.get("ir")
        session["search"] = search
        session["cate"] = cate
        session["low"] = low
        session["high"] = high
        session["sort"] = sort
        session["ir"] = ir
    elif status == "paging":
        search = request.values.get("search")
        cate = request.values.get("cate")
        low = splitlow(request.values.get("price"))
        high = splithigh(request.values.get("price"))
        sort = request.values.get("sort")
        ir = request.values.get("ir")
        if search is None:
            search = session.get("search")
        if cate is None:
            cate = session.get("cate")
        if low is None:
            low = session.get("low")
        if high is None:
            high = session.get("high")
        if sort is None:
            sort = session.get("sort")
        if ir is None:
            ir = session.get("ir")
        session["search"] = search
        session["cate"] = cate
        session["low"] = low
        session["high"] = high
        session["sort"] = sort
        session["ir"] = ir
    elif check_is_ir_search(status):
        search, cate, low, high, sort, ir = "non", "all", "non", "non", "non", status
    else:
        search, cate, low, high, sort, ir = "non", status, "non", "non", "non", "non"

    if cate != "all":
        res = db.session.query(Category).filter(Category.name == cate).first().products
    else:
        res = db.session.query(Product)

    if ir != "non":
        ts, selected_id = ir.split("_")[1:]
        target_path, target_img = load_from_cache(ts, selected_id, matting=True)
        rank = search_image(sess, target_img, ir_index)
        response = dict(
            selcted=selected_id,
            target_path="../" + target_path,
            n_show=ir_cfg['n_show'],
            matched=[])
        items = []
        for i, item in enumerate(rank[:ir_cfg['n_show']]):
            items.append(item[0])
        ordering = case(
            {key: index for index, key in enumerate(items)},
            value=Product.key
        )
        res = res.filter(Product.key.in_(items)).order_by(ordering)
    else:
        if search != "non":
            res = res.filter(Product.name.contains(search))
        if sort == "1":
            res = res.order_by(desc(Product.year))
        elif sort == "2":
            res = res.order_by(desc(Product.max_speed))
        elif sort == "3":
            res = res.order_by(Product.oil_consumption)
    ran = res.order_by(Product.price).all()
    if len(ran) != 0:
        left = ran[0].price
        right = ran[-1].price
    else:
        left, right = 0, 0
    if low != "non":
        res = res.filter(Product.price >= low).filter(Product.price <= high)
    else:
        low, high = left, right
    pagination = res.paginate(page, per_page=current_app.config['FLASKY_POST_PER_PAGE'], error_out=False)
    recommend = res.limit(3).all()
    products = pagination.items

    print(status, cate, search, sort, low, high, categories, cate_num, left, right)

    return render_template('shop.html', status=status, cate=cate, search=search, sort=sort, low=low, high=high, ir=ir,
                           categories=categories, cate_num=cate_num, left=str(left), right=str(right), pagination=pagination,
                           recommend=recommend, products=products)


def splitlow(price):
    if price is None:
        return None
    head = price.split("$")[1]
    res = head.split(" ")[0]
    return int(res)


def splithigh(price):
    if price is None:
        return None
    res = price.split("$")[2]
    return int(res)


@main.route('/blog/', methods=['POST', 'GET'])
def blog():
    blogs = Blog.query.filter(Blog.id != 0).order_by(Blog.id.desc()).all()
    return render_template('blog-index.html', blogs=blogs)


@main.route('/blog/single_blog/', methods=['POST', 'GET'])
def single_blog():
    return render_template('detail.html')


@main.route('/blog/<p>', methods=['POST', 'GET'])
@login_required
def blog_detail(p):
    blog = Blog.query.filter_by(id=p).first()
    num = Blog.query.count()
    pre = None
    next = None
    if int(p) > 1:
        pre = Blog.query.filter_by(id=int(p) - 1).first()
    if int(p) != num:
        next = Blog.query.filter_by(id=int(p) + 1).first()
    return render_template('blog-detail.html', blog=blog, pre=pre, next=next)


@main.route('/blog/comment', methods=['POST', 'GET'])
def blog_comment():
    text = request.form.get("text")
    # print(text)
    if text == '' or len(text) > 120:
        return "no"
    blog_id = request.form.get("blog_id")
    if current_user.is_authenticated:
        author_id = current_user.id
    else:
        author_id = '1'
    comment = BlogComment(body=text, author_id=author_id, blog_id=blog_id)
    db.session.add(comment)
    db.session.commit()
    return "ok"


@main.route('/blog/gustbook', methods=['POST', 'GET'])
def gustbook():
    blog = Blog.query.filter_by(id='0').first()
    return render_template('gustbook.html', blog=blog)


@main.route('/blog/add_blog', methods=['POST'])
@login_required
def add_blog():
    title = request.form.get('title')
    description = request.form.get('description')
    blog = Blog(title=title, content=description)

    images = []
    img1 = request.files.get('image1')
    images.append(img1)
    img2 = request.files.get('image2')
    images.append(img2)
    img3 = request.files.get('image3')
    images.append(img3)
    img4 = request.files.get('image4')
    images.append(img4)
    img5 = request.files.get('image5')
    images.append(img5)
    for img in images:
        if img.filename != '' and allow_file(img.filename):
            current_time = datetime.datetime.now().strftime('%H%M%S%Y%m%d')
            filename = current_time + random_string(8) + secure_filename(img.filename)
            file_path = os.path.join(Config.blog_direct, filename)
            img.save(file_path)
            blog.imagePaths.append(BlogImagePath(image_path='../static/img/blog/' + filename))

    db.session.add(blog)
    db.session.commit()
    return redirect(url_for('main.blog'))


@main.route('/blog/add', methods=['POST', 'GET'])
@login_required
def blog_add():
    return render_template('blog-add.html')


@main.route('/blog/update', methods=['POST', 'GET'])
def blog_update():
    return render_template('update.html')


@main.route('/blog/search', methods=['POST', 'GET'])
def blog_search():
    blogs = Blog.query.all()
    s = ''
    if request.method == 'POST':
        s = request.form.get('s')
        # print(s)
        if s != '':
            title_contain = Blog.query.filter(Blog.title.contains(s)).all()
            blogs = Blog.query.filter(Blog.content.contains(s)).all()
            for blog in title_contain:
                if blog not in blogs:
                    blogs.append(blog)
    return render_template('search.html', blogs=blogs, s=s)


@main.route('/about', methods=['POST', 'GET'])
def about():
    """
    View function for about info page
    """
    return render_template('about.html')


@main.route('/contact', methods=['POST', 'GET'])
def contact():
    """
    View function for contact page
    """
    return render_template('contact.html')


@main.route('/service', methods=['POST', 'GET'])
def services():
    """
    View function for service page
    """
    return render_template('service.html')


@main.route('/question', methods=['POST', 'GET'])
def question():
    """
    View function for question page
    """
    return render_template('faq.html')


@main.route('/cart', methods=['POST', 'GET'])
@login_required
def cart():
    """
    View function for user cart
    """
    _user = User.query.filter_by(id=current_user.id).first()
    flag = False  # flag for POST request
    if request.method == "POST":
        mode = request.values["mode"]
        product_id = int(request.values["prodid"])
        cart_item = db.session.query(
            Cart).filter(Cart.owner_id == _user.id).filter(Cart.product_id == product_id).first()
        # user edit the amount of the product
        if mode == "edit":
            product_num = int(request.values["prodnum"])
            cart_item.count = product_num
            db.session.add(cart_item)
            db.session.commit()
        # user remove the product from the cart
        elif mode == "remove":
            db.session.delete(cart_item)
            db.session.commit()
        # user select or cancel the selection of one product
        elif mode == "select":
            cart_item.is_selected = True if request.values["status"] == "True" else False
            db.session.add(cart_item)
            db.session.commit()
        else:
            pass
        flag = True
    # search the product in the cart that belong to the current user
    data = get_cart_items()
    if flag:
        output = price_calculator(data)
        output['count'] = len(data)
        return jsonify(output)
    return render_template('cart.html', data=data, price=price_calculator(data))


@main.route('/add_to_cart', methods=['POST', 'GET'])
@login_required
def add_to_cart():
    if request.method == "POST":
        product_id = int(request.values['product_id'])
        product_count = request.values['product_count']
        cart_item = db.session.query(
            Cart).filter(Cart.owner_id == current_user.id).filter(Cart.product_id == product_id).first()
        if cart_item is None:
            item = Cart(
                count=product_count,
                is_selected=True,
                owner_id=current_user.id,
                product_id=product_id
            )
            db.session.add(item)
            db.session.commit()
            data = get_cart_items()
            response = price_calculator(data)
            response['status'] = 0
            response['count'] = len(data)
            return jsonify(response)
        else:
            return jsonify({'product_id': product_id, 'product_count': product_count, 'status': 1})


@main.route('/checkout/<int:user_id>', methods=['POST', 'GET'])
def checkout(user_id):
    """
    View function for checkout page
    """
    # delivery_info_list = DeliveryInfo.query.filter_by(user_id=user_id).all()
    user_cart = Cart.query.filter_by(owner_id=user_id).filter_by(is_selected=True).all()
    product_pay = 0.0
    # total_weight = 0.0
    if len(user_cart) == 0:
        flash("No product selected!")
        return redirect(url_for("main.cart"))

    for c in user_cart:
        product_pay += c.product.price * c.product.discount * c.count
        # total_weight += c.product.weight * c.count
    # weight_pay = total_weight * 0.1
    # is_pandemic = Pandemic.query.first().is_pandemic
    return render_template('checkout.html', cart=user_cart,
                           product_pay=product_pay)


@main.route('/place_order/<int:buyer_id>/<int:pp>', methods=['POST', 'GET'])
def place_order(buyer_id, pp):
    if request.method == 'POST':
        start_date = request.form.get('start_date')
        start_time = change_time(request.form.get('start_time'), 0)
        st = datetime.datetime.strptime(start_date + " " + start_time, "%Y-%m-%d %H:%M:%S")
        note = request.form.get('note')
        product_ids = request.form.getlist('product')
        counts = request.form.getlist('count')
        flash_num = 0
        for i in range(0, len(product_ids)):
            product_aim = Product.query.filter_by(id=product_ids[i]).first()
            if product_aim.inventory - int(counts[i]) < 0:
                flash_num = 1
        if flash_num == 0:
            timestamp = datetime.datetime.utcnow()
            price = pp
            order = Order(
                timestamp=timestamp,
                pick_up_time=st,
                note=note,
                status='Created',
                price=price,
                buyer_id=buyer_id
            )
            db.session.add(order)
            db.session.commit()
            # order = Order.query.filter_by(buyer_id=buyer_id).filter_by(timestamp=timestamp).first()
            # print(order)
            for i in range(0, len(product_ids)):
                po = ProductOrder(
                    count=counts[i],
                    product_id=product_ids[i],
                    order_id=order.id
                )
                db.session.add(po)
                db.session.commit()
                po = ProductOrder.query.filter_by(product_id=product_ids[i]).filter_by(order_id=order.id).first()
                order.productOrders.append(po)
                cart_item = db.session.query(
                    Cart).filter(Cart.owner_id == current_user.id).filter(Cart.product_id == product_ids[i]).first()
                db.session.delete(cart_item)
                db.session.commit()
            db.session.commit()
            return redirect(url_for('main.account', user_id=buyer_id))
        else:
            flash('Sorry. The inventory of the product is not enough')
            return redirect(url_for('main.checkout', user_id=buyer_id))


@main.route('/account/<int:user_id>', methods=['POST', 'GET'])
@login_required
def account(user_id):
    """
    View function for checkout page
    """
    user = User.query.filter_by(id=user_id).first()
    return render_template('my-account.html', user=user)


@main.route('/my_order/<int:order_id>')
@login_required
def my_order(order_id):
    """
    View function for checkout page
    """
    order_aim = Order.query.filter_by(id=order_id).first()
    count_list = []
    product_list = []
    for item in order_aim.productOrders.all():
        p = Product.query.filter_by(id=item.product_id).first()
        count_list.append(item.count)
        product_list.append(p)
    product_zip = zip(count_list, product_list)
    return render_template('order.html', order=order_aim, product_zip=product_zip)


@main.route('/my_order_modify/', methods=['POST', 'GET'])
@login_required
def my_order_modify():
    if request.method == 'POST':
        order_id = request.form.get('order_id')
        phone_number = request.form.get('phone_number')
        country = request.form.get('country')
        city = request.form.get('city')
        street = request.form.get('street')
        detail = request.form.get('detail')
        order_aim = Order.query.filter_by(id=order_id).first()
        order_aim.phone_number = phone_number
        order_aim.country = country
        order_aim.city = city
        order_aim.street = street
        order_aim.detail = detail
        db.session.commit()
        return redirect(url_for('main.my_order', order_id=order_id))


@login_required
@main.route('/modify_avatar/', methods=['POST', 'GET'])
def modify_avatar():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        file = request.files.get('avatar')
        user = User.query.filter_by(id=user_id).first()
        if file and allow_file(file.filename):
            underling = random.randint(11, 99)
            filename = secure_filename(file.filename)
            # we create a new strong filename with random number, and the filename itself,
            # in case of name duplication
            strong_filename = str(underling) + filename
            file_path = os.path.join(Config.avatar_direct, strong_filename)
            file.save(file_path)
            user.avatar_path = '../../static/storage/avatars/' + strong_filename
            db.session.commit()
        else:
            flash('Invalid Image')
        return redirect(url_for('main.account', user_id=user_id))


@main.route('/wishlist', methods=['POST', 'GET'])
def wishlist():
    """
    View function for wishlist page
    """
    return render_template('wishlist.html')


@main.route('/single_product/<p>', methods=['POST', 'GET'])
def single_product(p):
    if current_user.is_authenticated:
        if int(p) in range(1, Product.query.count() + 1):
            p = p
        elif int(p) == 0:
            p = Product.query.count()
        else:
            p = 1
        product_all = []
        product = Product.query.filter_by(id=p).first()
        comments = Comment.query.filter_by(product_id=p).all()
        comments_show = comments[::-1]
        comments_num = len(comments)
        i = 0
        for category in product.categories:
            print("hello", category)
            for c in category.products:
                if c not in product_all:
                    i = i + 1
                    if i < 9:
                        product_all.append(c)
        if request.method == 'POST':
            if request.form.get('comment') is not None:
                user = User.query.filter_by(id=current_user.id).first()
                timestamp = datetime.datetime.now()
                body = request.form.get('comment')
                comment = Comment(author_id=user.id, timestamp=timestamp, product_id=p, body=body)
                db.session.add(comment)
                db.session.commit()
            else:
                user = User.query.filter_by(id=current_user.id).first()
                timestamp = datetime.datetime.utcnow()
                start_date = request.form.get('start_date')
                start_time = change_time(request.form.get('start_time'), 0)
                end_time = change_time(request.form.get('start_time'), 2)
                st = datetime.datetime.strptime(start_date+" "+start_time, "%Y-%m-%d %H:%M:%S")
                et = datetime.datetime.strptime(start_date+" "+end_time, "%Y-%m-%d %H:%M:%S")
                print('hello', st, timestamp)
                drive = Drive(
                    timestamp=timestamp,
                    drive_time_start=st,
                    drive_time_end=et,
                    note='Test Drive',
                    status='Created',
                    buyer_id=user.id
                )
                db.session.add(drive)
                db.session.commit()
                pd = ProductDrive(
                    count=1,
                    product_id=p,
                    drive_id=drive.id
                )
                db.session.add(pd)
                db.session.commit()
                pd = ProductDrive.query.filter_by(product_id=p).filter_by(
                    drive_id=drive.id).first()
                drive.productDrives.append(pd)
                db.session.commit()
            return redirect(url_for('main.single_product', p=p))
    else:
        flash('Please login before browsing products!')
        return redirect(url_for('auth.login'))
    return render_template('single-product.html', p2=product, product_all=product_all, comments=comments,
                           comments_num=comments_num, comments_show=comments_show)


def change_time(raw_time, offset):
    time_front = raw_time.split(" ")[0]
    time_end = raw_time.split(" ")[1]
    hour = int(time_front.split(":")[0])
    minute = time_front.split(":")[1]
    if time_end == "pm":
        hour = hour + 12 + offset
    elif time_end == "am":
        hour = hour + offset
    return str(hour) + ":" + minute + ":00"


# Cart Utils
def price_calculator(cart_dicts: list) -> dict:
    output = {
        "product_price": 0
    }
    for item in cart_dicts:
        if item["product_selected"]:
            output["product_price"] += item["product_price"] * item["product_discount"] * item["product_num"]
    return output


def get_cart_items() -> list:
    if current_user.is_authenticated:
        user_carts = Cart.query.filter_by(owner_id=current_user.id).all()
        # build the cart products list for GET request
        data = []
        for i, cart_item in enumerate(user_carts):
            _product = Product.query.filter_by(id=cart_item.product_id).first()
            data.append({
                "product_id": cart_item.product_id,
                "product_num": cart_item.count,
                "product_name": _product.name,
                "product_img": _product.imagePaths[0].resized_image_path,
                "product_desc": _product.description,
                "product_price": _product.price,
                "product_discount": _product.discount,
                "product_selected": cart_item.is_selected,
            })
        return data
    else:
        return []


def get_mini_cart_data():
    data = get_cart_items()
    n_items = len(data)
    if len(data) <= 3:
        return data, price_calculator(data), n_items
    else:
        return data[:3], price_calculator(data), n_items


def get_category_data():
    categories = Category.query.all()
    c = []
    for cat in categories:
        if len(list(cat.products)) != 0:
            c.append(cat.name)
    return c[:7]


ALLOWED_EXTENSIONS = {'gif', 'jpg', 'jpeg', 'png', 'GIF', 'JPG', 'PNG'}


# this method tests whether the file format is what we require
def allow_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def random_string(length):
    chars = 'abcdefghijklmnopqrstuvwxyz1234567890'
    return ''.join(random.choice(chars) for i in range(length))


# ================================ IR METHODS =============================

def get_ts():
    return str(calendar.timegm(time.gmtime()))





# ROUTE
@main.route("/ir_search", methods=['GET', 'POST'])
def ir_search():
    if request.method == 'POST':
        # generate ir link to shop
        if request.values['mode'] == "ir":
            ts = request.values['ts']
            selected_id = request.values['selected']
            return url_for('main.shop', status="irs_{}_{}".format(ts, selected_id))

        # response hci
        elif request.values['mode'] == "hci":
            # check if the post request has the file part
            if 'file' not in request.files:
                flash('No File Part')
                return redirect(request.url)
            file = request.files['file']
            if file.filename == '':
                flash('No Selected File')
                return redirect(request.url)
            if file:
                ts = get_ts()
                org_path = os.path.join(
                    flask_cfg['cache_cfg']['ir_hci']['prefix'],
                    flask_cfg['cache_cfg']['ir_hci']['org_middle'],
                    "{}_{}".format(ts, file.filename)
                )
                file.save(os.path.join(flask_cfg['static_path'], org_path))

                st = time.time()
                output = engine.infer(
                    os.path.join(flask_cfg['static_path'], org_path)
                )
                if output['status'] != 0:
                    return jsonify(output)

                response = build_response(output, ts)
                response['cfg'] = ir_hci_cfg['frontend_cfg']
                response['ts'] = ts

                print("IR HCI response time: {:.4f} seconds".format(time.time() - st))
                return jsonify(response)

    return render_template("shop.html")


def check_is_ir_search(c):
    if len(c.split("_")) != 3:
        return False
    if c[:3] != "irs":
        return False
    if len(c.split("_")[1]) != 10:
        return False
    return True
# =======================================================================
