from .dynamic_md5_node import DynamicCodeMD5

NODE_CLASS_MAPPINGS = {
    "DynamicCodeMD5": DynamicCodeMD5
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DynamicCodeMD5": "MD5动态加密"
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
