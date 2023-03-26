"""
Predefined Data for Testing
"""

ROLES = [
    {"id": 1, "name": "shop"}, {"id": 2, "name": "customer"}
]

CATEGORIES = [{"id": 1, "name": "bowed strings"}, {"id": 2, "name": "pucked strings"},
    {"id": 3, "name": "woodwinds"}, {"id": 4, "name": "brass"},
    {"id": 5, "name": "percussion"}, {"id": 6, "name": "keyboards"},
    {"id": 7, "name": "repairment"}, {"id": 8, "name": "maintenance"},
    {"id": 9, "name": "sound"}]

USERS = [
    {"id": 1, "email": "incognito@gmail.com", "username": "Incognito", "password": "123456", "role_id": 2, "confirmed": True,
     "avatar_path": '../static/img/no-image.png'},
    {"id": 2, "email": "bcd234@gmail.com", "username": "bcd234", "password": "123456", "role_id": 2, "confirmed": True,
     "avatar_path": "../static/storage/avatars/default_avatar.jpg"},
    {"id": 3, "email": "abc123@gmail.com", "username": "abc123", "password": "123456", "role_id": 1, "confirmed": True,
     "avatar_path": "../static/storage/avatars/default_avatar.jpg"},
    {"id": 4, "email": "wuyunze@gmail.com", "username": "wuyunze", "password": "123456", "role_id": 2, "confirmed": True,
     "avatar_path": "../static/storage/avatars/avatar_admin.jpg"},
]

PRODUCTS = [
    {"id": 1, "name": "piano1", "description": "This is a piano, none1 and none1", "weight": 200, "price": 199, "discount": 1, "inventory": 999},
    {"id": 2, "name": "piano2", "description": "This is a piano, none1 and none1", "weight": 200, "price": 299, "discount": 1, "inventory": 2999},
    {"id": 3, "name": "piano3", "description": "This is a piano, none1 and none1", "weight": 200, "price": 399, "discount": 1, "inventory": 1999},
    {"id": 4, "name": "piano4", "description": "This is a piano, none1 and none1", "weight": 200, "price": 1299, "discount": 1, "inventory": 1999},
    {"id": 5, "name": "piano5", "description": "This is a piano, none1 and none1", "weight": 200, "price": 1299, "discount": 1, "inventory": 1999},
    {"id": 6, "name": "piano6", "description": "This is a piano, none1 and none1", "weight": 200, "price": 1299, "discount": 1, "inventory": 1999},
    {"id": 7, "name": "piano7", "description": "This is a piano, none1 and none1", "weight": 200, "price": 1299, "discount": 1, "inventory": 1999},
    {"id": 8, "name": "piano8", "description": "This is a piano, none1 and none1", "weight": 200, "price": 1299, "discount": 1, "inventory": 1999},
    {"id": 9, "name": "piano9", "description": "This is a piano, none1 and none1", "weight": 200, "price": 1299, "discount": 1, "inventory": 1999},
    {"id": 10, "name": "piano10", "description": "This is a piano, none1 and none1", "weight": 200, "price": 1299, "discount": 1, "inventory": 1999},
    {"id": 11, "name": "piano11", "description": "This is a piano, none1 and none1", "weight": 200, "price": 1299, "discount": 1, "inventory": 1999},

    {"id": 12, "name": "drum1", "description": "This is a drum, none1 and none1", "weight": 50, "price": 1899, "discount": 1, "inventory": 399},
    {"id": 13, "name": "drum2", "description": "This is a drum, none1 and none1", "weight": 50, "price": 1799, "discount": 1, "inventory": 1929},
    {"id": 14, "name": "drum3", "description": "This is a drum, none1 and none1", "weight": 50, "price": 119, "discount": 1, "inventory": 1219},
    {"id": 15, "name": "drum4", "description": "This is a drum, none1 and none1", "weight": 50, "price": 149, "discount": 1, "inventory": 1979},
    {"id": 16, "name": "drum5", "description": "This is a drum, none1 and none1", "weight": 50, "price": 189, "discount": 1, "inventory": 7999},
    {"id": 17, "name": "drum6", "description": "This is a drum, none1 and none1", "weight": 50, "price": 189, "discount": 1, "inventory": 7999},
    {"id": 18, "name": "drum7", "description": "This is a drum, none1 and none1", "weight": 50, "price": 189, "discount": 1, "inventory": 7999},
    {"id": 19, "name": "drum8", "description": "This is a drum, none1 and none1", "weight": 50, "price": 189, "discount": 1, "inventory": 7999},
    {"id": 20, "name": "drum9", "description": "This is a drum, none1 and none1", "weight": 50, "price": 189, "discount": 1, "inventory": 7999},

    {"id": 21, "name": "wind1", "description": "This is a wind, none1 and none1", "weight": 8, "price": 189, "discount": 1, "inventory": 3999},
    {"id": 22, "name": "wind2", "description": "This is a wind, none1 and none1", "weight": 8, "price": 189, "discount": 1, "inventory": 3999},
    {"id": 23, "name": "wind3", "description": "This is a wind, none1 and none1", "weight": 8, "price": 189, "discount": 1, "inventory": 3999},
    {"id": 24, "name": "wind4", "description": "This is a wind, none1 and none1", "weight": 8, "price": 189, "discount": 1, "inventory": 3999},
    {"id": 25, "name": "wind5", "description": "This is a wind, none1 and none1", "weight": 8, "price": 189, "discount": 1, "inventory": 3999},
    {"id": 26, "name": "wind6", "description": "This is a wind, none1 and none1", "weight": 8, "price": 189, "discount": 1, "inventory": 3999},
    {"id": 27, "name": "wind7", "description": "This is a wind, none1 and none1", "weight": 8, "price": 189, "discount": 1, "inventory": 3999},
    {"id": 28, "name": "wind8", "description": "This is a wind, none1 and none1", "weight": 8, "price": 189, "discount": 1, "inventory": 3999},
    {"id": 29, "name": "wind9", "description": "This is a wind, none1 and none1", "weight": 8, "price": 189, "discount": 1, "inventory": 3999},
    {"id": 30, "name": "wind10", "description": "This is a wind, none1 and none1", "weight": 8, "price": 189, "discount": 1, "inventory": 3999},

    {"id": 31, "name": "violin cord", "description": "Adding cords and tuning", "weight": 0, "price": 189, "discount": 1, "inventory": 3999},
    {"id": 32, "name": "violin bridge", "description": "Replacement of the violin bridge", "weight": 0, "price": 189, "discount": 1, "inventory": 3999},
    {"id": 33, "name": "violin bow hair", "description": "Replacement of the violin bow hair", "weight": 0, "price": 189, "discount": 1, "inventory": 3999},
    {"id": 34, "name": "piano repairment", "description": "Replacement of key contact rubbers", "weight": 0, "price": 189, "discount": 1, "inventory": 3999},
    {"id": 35, "name": "brass maintenance", "description": "This includes cleaning instruments, tuning sliders, changing parts and giving maintenance advice", "weight": 0, "price": 189, "discount": 1, "inventory": 3999},
    {"id": 36, "name": "guitar maintenance", "description": "This includes cleaning instruments, adjusting strings, tuning and giving maintenance advice", "weight": 0, "price": 189, "discount": 1, "inventory": 3999},
    {"id": 37, "name": "drum maintenance","description": "This includes cleaning the instrument, lubing, changing the drum skin and giving maintenance advice", "weight": 0, "price": 189, "discount": 1, "inventory": 3999},
    {"id": 38, "name": "flute repairment", "description": "Check the flute and replace parts", "weight": 0, "price": 189, "discount": 1, "inventory": 3999},
    {"id": 39, "name": "digital piano repairment", "description": "Clean the internal dust and replace the circuit board", "weight": 0, "price": 189, "discount": 1, "inventory": 3999},
    {"id": 40, "name": "piano maintenance", "description": "This includes wiping the instrument, tuning, adjusting the movement and offering advice on maintenance", "weight": 0, "price": 189, "discount": 1, "inventory": 3999},
    {"id": 41, "name": "Xylophone-YX-500R", "description": "This is a household, elementary, small, short string, Tan xylophone", "weight": 30, "price": 200, "discount": 0.8, "inventory": 999},
    {"id": 42, "name": "Xylophone-YX-500F", "description": "This is a household, elementary, medium, short string, black xylophone", "weight": 30, "price": 200, "discount": 0.9, "inventory": 999},
    {"id": 43, "name": "Xylophone-YX-135", "description": "This is a professional, advanced, large, long string, Tan xylophone", "weight": 30, "price": 300, "discount": 0.8, "inventory": 999},
    {"id": 44, "name": "Xylophone-YX-35G", "description": "This is a professional, advanced, large, long string,  black xylophone", "weight": 30, "price": 300, "discount": 1, "inventory": 999},
    {"id": 45, "name": "Xylophone-YX-30G", "description": "This is a professional, advanced, large, short string, Tan xylophone", "weight": 30, "price": 300, "discount": 0.8, "inventory": 999},
    {"id": 46, "name": "steel piano-YG-250D", "description": "This is a household, elementary, small, light, black-and-white steel piano", "weight": 50, "price": 800, "discount": 0.7, "inventory": 999},
    {"id": 47, "name": "steel piano-YG-1210", "description": "This is a household, elementary, small, thick, black-and-white steel piano", "weight": 50, "price": 1000, "discount": 0.6, "inventory": 999},
    {"id": 48, "name": "steel piano-YG-2500", "description": "This is a professional, advanced, large, light, black and white steel piano", "weight": 70, "price": 5000, "discount": 0.8, "inventory": 999},
    {"id": 49, "name": "Vibrato-YV-2030MS", "description": "This is a professional, advanced, medium-sized, medium string, black-and-white vibraphone", "weight": 60, "price": 3000, "discount": 0.7, "inventory": 999},
    {"id": 50, "name": "Vibrato-YV-2700", "description": "This is a professional, advanced, medium-sized, short string, black-and-white vibraphone", "weight": 60, "price": 4000, "discount": 0.9, "inventory": 999},
    {"id": 51, "name": "Vibrato-YV-3710", "description": "This is a professional, advanced, medium-sized, medium string, black and yellow vibrato", "weight": 60, "price": 9000, "discount": 0.5, "inventory": 999},
    {"id": 52, "name": "Vibrato-YV-3910M", "description": "This is a professional, advanced, medium-sized, long string, black and yellow vibrato", "weight": 60, "price": 3000, "discount": 1, "inventory": 999},
    {"id": 53, "name": "Vibrato-YV-4110M", "description": "This is a professional, advanced, large-sized, medium string, black and yellow vibrato", "weight": 80, "price": 4000, "discount": 1, "inventory": 999},
    {"id": 54, "name": "tube clock-YCH-6018", "description": "This is a professional, advanced, small, short string, copper tube clock", "weight": 50, "price": 500, "discount": 0.9, "inventory": 999},
    {"id": 55, "name": "tube clock-YCH-7018", "description": "This is a professional, advanced, large, long string, copper tube clock", "weight": 50, "price": 800, "discount": 1, "inventory": 999},
    {"id": 56, "name": "Military drum-CB-9000", "description": "This is a professional, advanced, large, thick, red drum", "weight": 70, "price": 300, "discount": 0.8, "inventory": 999},
    {"id": 57, "name": "Military drum-CB-8000", "description": "This is a professional, advanced, large, medium, red drum", "weight": 65, "price": 250, "discount": 1, "inventory": 999},
    {"id": 58, "name": "Military drum-CB-7000", "description": "This is a professional, advanced, large, light, red drum", "weight": 60, "price": 200, "discount": 1, "inventory": 999},
    {"id": 59, "name": "Military drum-CSM", "description": "This is a professional, advanced, small, light, yellow drum", "weight": 30, "price": 100, "discount": 1, "inventory": 999},
    {"id": 60, "name": "Military drum-OSM", "description": "This is a professional, advanced, small, light, red drum", "weight": 30, "price": 200, "discount": 0.9, "inventory": 999},
    {"id": 61, "name": "Combined drum-TP-3300R", "description": "This is a household, elementary, medium-sized, metal colored, copper combination drum", "weight": 80, "price": 800, "discount": 1, "inventory": 999},
    {"id": 62, "name": "Combined drum-TP-4300R", "description": "This is a household, elementary, medium-sized, metallic and alloy combination drum", "weight": 80, "price": 850, "discount": 0.8, "inventory": 999},
    {"id": 63, "name": "Combined drum-TP-6300R", "description": "This is a professional, advanced, large, metal colored, copper combination drum", "weight": 80, "price": 900, "discount": 0.9, "inventory": 999},
    {"id": 64, "name": "Combined drum-TP-7300R", "description": "This is a professional, advanced, large, metallic and alloy combination drum", "weight": 100, "price": 2000, "discount": 0.6, "inventory": 999},
    {"id": 65, "name": "Earphone-W-E3A-1", "description": "This is a household, small, in ear, noise reduction black headset", "weight": 2, "price": 50, "discount": 0.8, "inventory": 999},
    {"id": 66, "name": "Earphone-W-E3B-2", "description": "This is a household, small, in ear, noise reduction purple headset", "weight": 2, "price": 60, "discount": 0.9, "inventory": 999},
    {"id": 67, "name": "Earphone-W-E5B-2", "description": "This is a household, small, in ear, noise reduction brown headset", "weight": 2, "price": 60, "discount": 0.8, "inventory": 999},
    {"id": 68, "name": "Earphone-YH-E500A-2", "description": "This is a household, large, head worn, non noise reducing black earphone", "weight": 10, "price": 200, "discount": 0.9, "inventory": 999},
    {"id": 69, "name": "Earphone-YH-E500A-1", "description": "This is a household, large, head worn, noise reducing black earphone", "weight": 10, "price": 200, "discount": 1, "inventory": 99},
    {"id": 70, "name": "Earphone-YH-E700A-1", "description": "This is a household, medium-sized, head worn, noise reducing black earphone", "weight": 19, "price": 250, "discount": 1, "inventory": 99},
    {"id": 71, "name": "Earphone-HPH-MT7", "description": "This is a professional, medium-sized, noise reducing black headset", "weight": 15, "price": 400, "discount": 1, "inventory": 99},
    {"id": 72, "name": "Earphone-HPH-MT7W", "description": "This is a professional, medium-sized, noise reducing white headset", "weight": 15, "price": 500, "discount": 1, "inventory": 99},
    {"id": 73, "name": "Earphone-HPH-MT8", "description": "This is a professional, medium-sized, head worn, noise free black headset", "weight": 15, "price": 290, "discount": 1, "inventory": 99},
    {"id": 74, "name": "Earphone-HPH-MT9", "description": "This is a professional, large, head worn, noise reducing black headset", "weight": 15, "price": 400, "discount": 1, "inventory": 99},
    {"id": 75, "name": "Earphone-HPH-MT9W", "description": "This is a professional, large, headset, noise reduction white headset", "weight": 15, "price": 600, "discount": 1, "inventory": 99},
    {"id": 76, "name": "Speaker-NS-AW350", "description": "This is a household, small, wired and reliable white speaker", "weight": 30, "price": 50, "discount": 1, "inventory": 99},
    {"id": 77, "name": "Speaker-NS-AW190", "description": "This is a household, medium-sized, wired and reliable white speaker", "weight": 40, "price": 60, "discount": 1, "inventory": 99},
    {"id": 78, "name": "Speaker-NS-AW570", "description": "This is a professional, large, wired and reliable white speaker", "weight": 50, "price": 80, "discount": 1, "inventory": 99},
    {"id": 79, "name": "Speaker-NS-AW1941", "description": "This is a professional, medium-sized, wired and reliable white speaker", "weight": 40, "price": 95, "discount": 1, "inventory": 99},
    {"id": 80, "name": "Speaker-NS-AW1942", "description": "This is a professional, medium-sized, wireless and reliable white speaker", "weight": 40, "price": 79, "discount": 1, "inventory": 99},
]

PRODUCTS2CATEGORIES = [
    {"product_id": 1, "category_ids": [6]},
    {"product_id": 2, "category_ids": [6]},
    {"product_id": 3, "category_ids": [6]},
    {"product_id": 4, "category_ids": [6]},
    {"product_id": 5, "category_ids": [6]},
    {"product_id": 6, "category_ids": [6]},
    {"product_id": 7, "category_ids": [6]},
    {"product_id": 8, "category_ids": [6]},
    {"product_id": 9, "category_ids": [6]},
    {"product_id": 10, "category_ids": [6]},
    {"product_id": 11, "category_ids": [6]},

    {"product_id": 12, "category_ids": [5]},
    {"product_id": 13, "category_ids": [5]},
    {"product_id": 14, "category_ids": [5]},
    {"product_id": 15, "category_ids": [5]},
    {"product_id": 16, "category_ids": [5]},
    {"product_id": 17, "category_ids": [5]},
    {"product_id": 18, "category_ids": [5]},
    {"product_id": 19, "category_ids": [5]},
    {"product_id": 20, "category_ids": [5]},

    {"product_id": 21, "category_ids": [3]},
    {"product_id": 22, "category_ids": [3]},
    {"product_id": 23, "category_ids": [3]},
    {"product_id": 24, "category_ids": [3]},
    {"product_id": 25, "category_ids": [3]},
    {"product_id": 26, "category_ids": [3]},
    {"product_id": 27, "category_ids": [3]},
    {"product_id": 28, "category_ids": [3]},
    {"product_id": 29, "category_ids": [3]},
    {"product_id": 30, "category_ids": [3]},
    {"product_id": 31, "category_ids": [7]},
    {"product_id": 32, "category_ids": [7]},
    {"product_id": 33, "category_ids": [7]},
    {"product_id": 34, "category_ids": [7]},
    {"product_id": 35, "category_ids": [8]},
    {"product_id": 36, "category_ids": [8]},
    {"product_id": 37, "category_ids": [8]},
    {"product_id": 38, "category_ids": [7]},
    {"product_id": 39, "category_ids": [7]},
    {"product_id": 40, "category_ids": [8]},
    {"product_id": 41, "category_ids": [5]},
    {"product_id": 41, "category_ids": [5]},
    {"product_id": 42, "category_ids": [5]},
    {"product_id": 43, "category_ids": [5]},
    {"product_id": 44, "category_ids": [5]},
    {"product_id": 45, "category_ids": [5]},
    {"product_id": 46, "category_ids": [5]},
    {"product_id": 47, "category_ids": [5]},
    {"product_id": 48, "category_ids": [5]},
    {"product_id": 49, "category_ids": [5]},
    {"product_id": 50, "category_ids": [5]},
    {"product_id": 51, "category_ids": [5]},
    {"product_id": 52, "category_ids": [5]},
    {"product_id": 53, "category_ids": [5]},
    {"product_id": 54, "category_ids": [5]},
    {"product_id": 55, "category_ids": [5]},
    {"product_id": 56, "category_ids": [5]},
    {"product_id": 57, "category_ids": [5]},
    {"product_id": 58, "category_ids": [5]},
    {"product_id": 59, "category_ids": [5]},
    {"product_id": 60, "category_ids": [5]},
    {"product_id": 61, "category_ids": [5]},
    {"product_id": 62, "category_ids": [5]},
    {"product_id": 63, "category_ids": [5]},
    {"product_id": 64, "category_ids": [5]},
    {"product_id": 65, "category_ids": [9]},
    {"product_id": 66, "category_ids": [9]},
    {"product_id": 67, "category_ids": [9]},
    {"product_id": 68, "category_ids": [9]},
    {"product_id": 69, "category_ids": [9]},
    {"product_id": 70, "category_ids": [9]},
    {"product_id": 71, "category_ids": [9]},
    {"product_id": 72, "category_ids": [9]},
    {"product_id": 73, "category_ids": [9]},
    {"product_id": 74, "category_ids": [9]},
    {"product_id": 75, "category_ids": [9]},
    {"product_id": 76, "category_ids": [9]},
    {"product_id": 77, "category_ids": [9]},
    {"product_id": 78, "category_ids": [9]},
    {"product_id": 79, "category_ids": [9]},
    {"product_id": 80, "category_ids": [9]},
]

CARTS = [
    {"id": 1, "count": 2, "owner_id": 2, "product_id": 1, "is_selected": True},
    {"id": 2, "count": 3, "owner_id": 2, "product_id": 3, "is_selected": False},
    {"id": 3, "count": 1, "owner_id": 2, "product_id": 4, "is_selected": True},
    {"id": 4, "count": 2, "owner_id": 2, "product_id": 7, "is_selected": True},
]

PRODUCTIMAGEPATHS = [
    {"id": 1, "image_path": "../../static/storage/products/1043492022041147gp_product_gb1_989f849fc2692767106a8e9604ef9377.jpg", "product_id": 1},
    {"id": 2, "image_path": "../../static/storage/products/1044242022041134gp_product_gb1_989f849fc2692767106a8e9604ef9377.jpg", "product_id": 2},
    {"id": 3, "image_path": "../../static/storage/products/1058172022041138gp_product_c5x_91c04cb3e0e2f29847331c203c986614.jpg", "product_id": 3},
    {"id": 4, "image_path": "../../static/storage/products/1058352022041136gp_product_CF6_c0895dd5de951ac136e6d5dc04862a56.jpg", "product_id": 4},
    {"id": 5, "image_path": "../../static/storage/products/1058522022041192gp_product_s6x_2578a85a25d71f69c7dadf5cd592dd84.jpg", "product_id": 5},
    {"id": 6, "image_path": "../../static/storage/products/1059132022041196gp_product_s6x_2578a85a25d71f69c7dadf5cd592dd84.jpg", "product_id": 6},
    {"id": 7, "image_path": "../../static/storage/products/1058522022041192gp_product_s6x_2578a85a25d71f69c7dadf5cd592dd84.jpg", "product_id": 7},
    {"id": 8, "image_path": "../../static/storage/products/1059132022041196gp_product_s6x_2578a85a25d71f69c7dadf5cd592dd84.jpg", "product_id": 8},
    {"id": 9, "image_path": "../../static/storage/products/1058522022041192gp_product_s6x_2578a85a25d71f69c7dadf5cd592dd84.jpg", "product_id": 9},
    {"id": 10, "image_path": "../../static/storage/products/1059132022041196gp_product_s6x_2578a85a25d71f69c7dadf5cd592dd84.jpg", "product_id": 10},
    {"id": 11, "image_path": "../../static/storage/products/1059132022041196gp_product_s6x_2578a85a25d71f69c7dadf5cd592dd84.jpg", "product_id": 11},

    {"id": 12, "image_path": "../../static/storage/products/64357834534654357___-1.jpg", "product_id": 12},
    {"id": 13, "image_path": "../../static/storage/products/4687326536537_thumb_011.jpg", "product_id": 13},
    {"id": 14, "image_path": "../../static/storage/products/64723463876536573_thumb_0021.png", "product_id": 14},
    {"id": 15, "image_path": "../../static/storage/products/743534867537_thumb_11.jpg", "product_id": 15},
    {"id": 16, "image_path": "../../static/storage/products/12790846347956_thumb_a2.jpg", "product_id": 16},
    {"id": 17, "image_path": "../../static/storage/products/35467324587_Hybrid_Maple_540x540_735x735_9a1491d206e417dabe25ffb9a7256e44.jpg", "product_id": 17},
    {"id": 18, "image_path": "../../static/storage/products/347638754576357_2.jpg", "product_id": 18},
    {"id": 19, "image_path": "../../static/storage/products/462374658237_thumb_EEC3B1474CC2FF84F87750513DCFE138.jpg", "product_id": 19},
    {"id": 20, "image_path": "../../static/storage/products/463287567354_540x540_396x396_88f34b4b488bd561277141e6457f8ce5.jpg", "product_id": 20},

    {"id": 21, "image_path": "../../static/storage/products/64357834534654357__.jpg", "product_id": 21},
    {"id": 22, "image_path": "../../static/storage/products/64357834534654357__(1).jpg", "product_id": 22},
    {"id": 23, "image_path": "../../static/storage/products/64357834534654357____(1).jpg", "product_id": 23},
    {"id": 24, "image_path": "../../static/storage/products/64357834534654357____(2).jpg", "product_id": 24},
    {"id": 25, "image_path": "../../static/storage/products/64357834534654357______(1).jpg", "product_id": 25},
    {"id": 26, "image_path": "../../static/storage/products/64357834534654357cus.jpg", "product_id": 26},
    {"id": 27, "image_path": "../../static/storage/products/64357834534654357cus(1).jpg", "product_id": 27},
    {"id": 28, "image_path": "../../static/storage/products/a3f7b6565ee7.jpg", "product_id": 28},
    {"id": 29, "image_path": "../../static/storage/products/ee91d6d94ef9.jpg", "product_id": 29},
    {"id": 30, "image_path": "../../static/storage/products/fd1f5e44dcd5.jpg", "product_id": 30},
    {"id": 31, "image_path": "../../static/storage/products/violin_repair.jpg", "product_id": 31},
    {"id": 32, "image_path": "../../static/storage/products/Violin-Bridge-90-degree-angle.jpg", "product_id": 32},
    {"id": 33, "image_path": "../../static/storage/products/How-To-Replace-Your-Instruments-Bow-Hair-Index.jpg", "product_id": 33},
    {"id": 34, "image_path": "../../static/storage/products/85dcd0058981814a5f8e51052fce8f7f.jpg", "product_id": 34},
    {"id": 35, "image_path": "../../static/storage/products/Repair_03.jpg", "product_id": 35},
    {"id": 36, "image_path": "../../static/storage/products/repair-header.jpg", "product_id": 36},
    {"id": 37, "image_path": "../../static/storage/products/Drum-maintenance-hero-Copy.jpg", "product_id": 37},
    {"id": 38, "image_path": "../../static/storage/products/Cambridge_Woodwind_Makers_Flute_Repair_And_Care_course_with_Daniel_Bangham-e1559307146975-scaled-e1645459533582.jpg", "product_id": 38},
    {"id": 39, "image_path": "../../static/storage/products/How-to-Fix-Digital-Piano-Keys.jpg", "product_id": 39},
    {"id": 40, "image_path": "../../static/storage/products/How-to-Care-for-Your-Piano-5-1200x1800.jpg", "product_id": 40},
    {"id": 41, "image_path": "../../static/storage/products/YX-500R.jpg","product_id": 41},
    {"id": 42, "image_path": "../../static/storage/products/YX-500F.jpg", "product_id": 42},
    {"id": 43, "image_path": "../../static/storage/products/YX-135.jpg", "product_id": 43},
    {"id": 44, "image_path": "../../static/storage/products/YX-35G.jpg", "product_id": 44},
    {"id": 45, "image_path": "../../static/storage/products/YX-30G.jpg", "product_id": 45},
    {"id": 46, "image_path": "../../static/storage/products/YG-250D.jpg", "product_id": 46},
    {"id": 47, "image_path": "../../static/storage/products/YG-1210.jpg", "product_id": 47},
    {"id": 48, "image_path": "../../static/storage/products/YG-2500.jpg", "product_id": 48},
    {"id": 49, "image_path": "../../static/storage/products/YV-2030MS.jpg", "product_id": 49},
    {"id": 50, "image_path": "../../static/storage/products/YV-2700.jpg", "product_id": 50},
    {"id": 51, "image_path": "../../static/storage/products/YV-3710.jpg", "product_id": 51},
    {"id": 52, "image_path": "../../static/storage/products/YV-3910M.jpg", "product_id": 52},
    {"id": 53, "image_path": "../../static/storage/products/YV-4110M.jpg", "product_id": 53},
    {"id": 54, "image_path": "../../static/storage/products/YCH-6018.jpg", "product_id": 54},
    {"id": 55, "image_path": "../../static/storage/products/YCH-7018.jpg", "product_id": 55},
    {"id": 56, "image_path": "../../static/storage/products/CB-9000.jpg", "product_id": 56},
    {"id": 57, "image_path": "../../static/storage/products/CB-8000.jpg", "product_id": 57},
    {"id": 58, "image_path": "../../static/storage/products/CB-7000.jpg", "product_id": 58},
    {"id": 59, "image_path": "../../static/storage/products/CSM.jpg", "product_id": 59},
    {"id": 60, "image_path": "../../static/storage/products/OSM.jpg", "product_id": 60},
    {"id": 61, "image_path": "../../static/storage/products/OSM.jpg", "product_id": 61},
    {"id": 62, "image_path": "../../static/storage/products/TP-4300R.jpg", "product_id": 62},
    {"id": 63, "image_path": "../../static/storage/products/TP-6300R.jpg", "product_id": 63},
    {"id": 64, "image_path": "../../static/storage/products/TP-7300R.jpg", "product_id": 64},
    {"id": 65, "image_path": "../../static/storage/products/W-E3A-1.png", "product_id": 65},
    {"id": 66, "image_path": "../../static/storage/products/W-E3B-2.jpg", "product_id": 66},
    {"id": 67, "image_path": "../../static/storage/products/W-E5B-2.jpg", "product_id": 67},
    {"id": 68, "image_path": "../../static/storage/products/homeYH-L700A-2.jpg", "product_id": 68},
    {"id": 69, "image_path": "../../static/storage/products/homeYH-E500A-1.jpg", "product_id": 69},
    {"id": 70, "image_path": "../../static/storage/products/homeYH-E700A-1.jpg", "product_id": 70},
    {"id": 71, "image_path": "../../static/storage/products/proHPH-MT7.jpg", "product_id": 71},
    {"id": 72, "image_path": "../../static/storage/products/proHPH-MT7W.jpg", "product_id": 72},
    {"id": 73, "image_path": "../../static/storage/products/proHPH-MT8.jpg", "product_id": 73},
    {"id": 74, "image_path": "../../static/storage/products/proHPH-MT9.jpg", "product_id": 74},
    {"id": 75, "image_path": "../../static/storage/products/proHPH-MT9W.jpg", "product_id": 75},
    {"id": 76, "image_path": "../../static/storage/products/NS-AW350.jpg", "product_id": 76},
    {"id": 77, "image_path": "../../static/storage/products/NS-AW190.jpg", "product_id": 77},
    {"id": 78, "image_path": "../../static/storage/products/NS-AW570.jpg", "product_id": 78},
    {"id": 79, "image_path": "../../static/storage/products/NS-AW1941.jpg", "product_id": 79},
    {"id": 80, "image_path": "../../static/storage/products/NS-AW1942.jpg", "product_id": 80},
]

DELIVERYINFOS = [
    {"id": 1, "name": "Ren", "gender": 1, "phone_number": 838383, "country": "China", "city": "HongKong",
     "street": "Handsome", "detail": "702", "user_id": 2},
    {"id": 2, "name": "Geng", "gender": 2, "phone_number": 949494, "country": "Spain", "city": "Madrid",
     "street": "Han", "detail": "1602", "user_id": 2}
]

BLOGS = [
    {"id": 11, "title": "Guest Book", "content": "None", "author_id": 3},
    {"id": 1, "title": "Saxophone", "content": "This is a saxophone...", "author_id": 3},
    {"id": 2, "title": "I Hate Drums", "content": "I hate playing drums when I was...", "author_id": 3},
    {"id": 3, "title": "I Love Drums", "content": "I Love drums a lot. Back to...", "author_id": 3},
    {"id": 4, "title": "You can post blog WITHOUT IMAGE", "content": "I just found image is not necessary for a blog...", "author_id": 3},
    {"id": 5, "title": "Brass Is My Favorite", "content": "The sounds made by brasses are amazing...", "author_id": 3},
    {"id": 6, "title": "Brass Sounds Awful", "content": "I would rather use woods instead of brasses...", "author_id": 3},
    {"id": 7, "title": "I Love Piano", "content": "Piano probably is the best instrument...", "author_id": 3},
    {"id": 8, "title": "Piano is TOO DIFFICULT", "content": "Piano probably is the most difficult instrument...", "author_id": 3},
    {"id": 9, "title": "Cornet vs Trumpet | What's the difference?", "author_id": 3,
     "content": "Before we look at the difference, let’s first cover the basic elements of their design that are identical. Firstly, and most obviously, they are both made of the same material, Brass, have 3 valves and the sound is produced on both by ‘buzzing’ your lips. The tubing is also of an identical length (4 1/2 ft approx without valves depressed), although it is wound much tighter on a Cornet giving the initial appearance that it is shorter. As they are both the same length they therefore also play at the same pitch which is Bb on standard models."},
    {"id": 10, "title": "Briefly Noted: Alice Coote Schubertiade", "author_id": 3,
     "content": "At the end of March here in Washington, Alice Coote was the best part of the National Symphony Orchestra's performance of Mahler's Second Symphony, led by Michael Tilson Thomas. The British mezzo-soprano recorded this selection of twenty-one Schubert songs, back in December of 2017, in All Saints’ Church, East Finchley, in London. The program is a mixture of rather simple strophic songs and more complex pieces, some relative rarities alongside some of the most often heard songs in performances with new ideas to recommend them."}
]

BLOGIMAGEPATHS = [
    {"id": 1, "image_path": "../../static/img/blog/81v9wttUWbL._SX425_.jpg", "blog_id": 10},
    {"id": 2, "image_path": "../../static/img/blog/trumpet-facts_88be0d82-b6a7-4ffb-ace0-01c85aa3a7c7_600x.jpeg", "blog_id": 9},
    {"id": 3, "image_path": "../../static/img/blog/trumpet-bands.jpeg", "blog_id": 9},
    {"id": 4, "image_path": "../../static/img/blog/ptrumpet-learn.jpeg", "blog_id": 9},
    {"id": 5, "image_path": "../../static/img/blog/cornet-younger-people.jpeg", "blog_id": 9},
    {"id": 6, "image_path": "../../static/storage/products/1059132022041196gp_product_s6x_2578a85a25d71f69c7dadf5cd592dd84.jpg", "blog_id": 7},
    {"id": 11, "image_path": "../../static/storage/products/1059132022041196gp_product_s6x_2578a85a25d71f69c7dadf5cd592dd84.jpg", "blog_id": 8},
    {"id": 12, "image_path": "../../static/storage/products/64357834534654357___-1.jpg", "blog_id": 3},
    {"id": 13, "image_path": "../../static/storage/products/4687326536537_thumb_011.jpg", "blog_id": 3},
    {"id": 14, "image_path": "../../static/storage/products/64723463876536573_thumb_0021.png", "blog_id": 3},
    {"id": 15, "image_path": "../../static/storage/products/743534867537_thumb_11.jpg", "blog_id": 3},
    {"id": 16, "image_path": "../../static/storage/products/12790846347956_thumb_a2.jpg", "blog_id": 2},
    {"id": 17, "image_path": "../../static/storage/products/35467324587_Hybrid_Maple_540x540_735x735_9a1491d206e417dabe25ffb9a7256e44.jpg", "blog_id": 2},
    {"id": 18, "image_path": "../../static/storage/products/347638754576357_2.jpg", "blog_id": 2},
    {"id": 19, "image_path": "../../static/storage/products/462374658237_thumb_EEC3B1474CC2FF84F87750513DCFE138.jpg", "blog_id": 2},
    {"id": 20, "image_path": "../../static/storage/products/463287567354_540x540_396x396_88f34b4b488bd561277141e6457f8ce5.jpg", "blog_id": 2},
    {"id": 21, "image_path": "../../static/storage/products/64357834534654357__.jpg", "blog_id": 5},
    {"id": 22, "image_path": "../../static/storage/products/64357834534654357__(1).jpg", "blog_id": 5},
    {"id": 23, "image_path": "../../static/storage/products/64357834534654357____(1).jpg", "blog_id": 5},
    {"id": 24, "image_path": "../../static/storage/products/64357834534654357____(2).jpg", "blog_id": 5},
    {"id": 25, "image_path": "../../static/storage/products/64357834534654357______(1).jpg", "blog_id": 5},
    {"id": 26, "image_path": "../../static/storage/products/64357834534654357cus.jpg", "blog_id": 6},
    {"id": 27, "image_path": "../../static/storage/products/64357834534654357cus(1).jpg", "blog_id": 6},
    {"id": 28, "image_path": "../../static/storage/products/a3f7b6565ee7.jpg", "blog_id": 6},
    {"id": 29, "image_path": "../../static/storage/products/ee91d6d94ef9.jpg", "blog_id": 6},
    {"id": 30, "image_path": "../../static/storage/products/fd1f5e44dcd5.jpg", "blog_id": 1}
]

BLOGCOMMENTS = [
    {"id": 1, "body": "Hello", "blog_id": 1, "author_id": 3},
    {"id": 2, "body": "That's great", "blog_id": 2, "author_id": 3},
    {"id": 3, "body": "Awesome", "blog_id": 3, "author_id": 3},
    {"id": 4, "body": "Good", "blog_id": 4, "author_id": 3},
    {"id": 5, "body": "Ohhh, no", "blog_id": 5, "author_id": 3},
    {"id": 6, "body": "OK", "blog_id": 6, "author_id": 3},
    {"id": 7, "body": "Yeah", "blog_id": 7, "author_id": 3},
    {"id": 8, "body": "lol", "blog_id": 8, "author_id": 3}
]

ORDERS = [
    {"id": 1, "note": "Please be careful", "status": "Packing",
     "ship_way": "Delivery", "price": 3957, "name": "Ronnie", "gender": 1, "phone_number": 8848, "country": "China",
     "city": "Beijing", "street": "Youan", "detail": "building33", "priority": 1, "buyer_id": 2},
    {"id": 2, "note": "Please be vigilant", "status": "Created",
     "ship_way": "Delivery", "price": 2101, "name": "Er", "gender": 2, "phone_number": 88488, "country": "Spain",
     "city": "Madrid", "street": "Han", "detail": "1602", "priority": 0, "buyer_id": 2}
]

PRODUCTORDERS = [
    {"id": 1, "count": 1, "product_id": 4, "order_id": 1},
    {"id": 2, "count": 2, "product_id": 7, "order_id": 1},
    {"id": 3, "count": 2, "product_id": 66, "order_id": 2},
    {"id": 4, "count": 1, "product_id": 39, "order_id": 2},
    {"id": 5, "count": 1, "product_id": 13, "order_id": 2}
]
