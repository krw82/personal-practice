config = {
    "model": "example-model",
    "temperature": 0.2,
    "max_tokens": 800,
}
config["timeout"] =30
config["retry_count"] = 2
print("재시도 횟수:", config["retry_count"])
print("모델:", config["model"])
print("최대 토큰:", config["max_tokens"])
print("실행 설정:", config)