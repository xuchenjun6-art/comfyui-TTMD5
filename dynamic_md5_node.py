import hashlib
from datetime import datetime


class DynamicCodeMD5:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "dynamic_code": ("STRING", {"default": "", "multiline": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "generate"
    CATEGORY = "TT专用"

    def generate(self, dynamic_code):
        now = datetime.now()
        minute_bucket = (now.minute // 10) * 10
        time_part = f"{now.year:04d}{now.month:02d}{now.day:02d}{now.hour:02d}{minute_bucket:02d}"
        source = f"{dynamic_code}{time_part}"
        md5_value = hashlib.md5(source.encode("utf-8")).hexdigest()
        return (md5_value,)
