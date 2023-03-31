import os

proj_path = "D:/ProjectGross/PycharmProjects/FYP/app"

flask_cfg = dict(
    static_path=os.path.join(proj_path, "static"),
    cache_cfg=dict(
        cache_path="cache",
        ir_hci=dict(
            prefix='cache/ir',
            im_middle='images-clip',
            m_middle='masks-clip',
            org_middle='images-org',
            rs_middle='images-rs'
        )
    )
)
