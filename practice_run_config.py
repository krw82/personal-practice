config = {
    "model": "example-model",
    "temperature": 0.2,
    "max_tokens": 800,
}
config["timeout"] =30
print("모델:", config["model"])
print("최대 토큰:", config["max_tokens"])