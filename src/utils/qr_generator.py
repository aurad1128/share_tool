# -*- coding: utf-8 -*-
"""
二维码生成器
"""

import io
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from PIL import ImageColor


def generate_qr(data, size=200, color='#E0687A'):
    """生成二维码 QPixmap"""
    from PyQt5.QtGui import QPixmap

    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=2,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # 生成带圆角的粉色二维码
    img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=RoundedModuleDrawer(),
        fill_color=ImageColor.getcolor(color, 'RGB'),
        back_color='white',
    )

    # 转为 QPixmap
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    buf.seek(0)

    pixmap = QPixmap()
    pixmap.loadFromData(buf.read())
    buf.close()

    if pixmap.width() > 0:
        pixmap = pixmap.scaled(size, size)

    return pixmap
