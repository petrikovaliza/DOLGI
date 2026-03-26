class TemporaryValue:
    def __init__(self, obj, attr, new_value):
        self.obj = obj
        self.attr = attr
        self.new_value = new_value
        self.old_value = None
    
    def __enter__(self):
        self.old_value = getattr(self.obj, self.attr)
        setattr(self.obj, self.attr, self.new_value)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        setattr(self.obj, self.attr, self.old_value)


class Config:
    setting = "old"


cfg = Config()
print(f"Before: {cfg.setting}")

with TemporaryValue(cfg, "setting", "new"):
    print(f"Inside: {cfg.setting}")

print(f"After: {cfg.setting}")