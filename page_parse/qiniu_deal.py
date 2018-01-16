# coding=utf-8
from qiniu import Auth, BucketManager
import os


def save2qiniu(key, img_src):

    # 需要填写你的 Access Key 和 Secret Key
    access_key = os.getenv("AK")
    secret_key = os.getenv("SK")

    # 构建鉴权对象
    q = Auth(access_key, secret_key)
    bucket = BucketManager(q)
    # 要上传的空间
    bucket_name = os.getenv("SPACE")
    # 上传到七牛后保存的文件名 key
    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, key, 3600)

    ret, info = bucket.fetch(img_src, bucket_name, key)
    print(info)
    assert ret['key'] == key
