print("Hello, dear user! Welcome to AI api! (Notice: this API DO NOT have memory.)")

import argparse

def main(arg1,arg2):
    import requests
    import json
    url = "https://api.theb.ai/v1/chat/completions"
# url = "https://api.baizhi.ai/v1/chat/completions"
    if arg1=="35t":
        mol="gpt-3.5-turbo"
    elif arg1=="4":
        mol="gpt-4"
    else:
        print("Invalid model")
        return
    payload = json.dumps({"model": mol,"messages": [{"role": "user","content": arg2}],"stream": False})
    headers = {
        'Authorization': 'Bearer sk-SCTZF4w8GFy07tpgmJDPVGhlQi5BSQA4tusj4TtW9oDK47gK',
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    jsonized = response.json()
    try:
        #if(mol=="gpt-4"):
            #print(jsonized)
        print(mol+": "+jsonized["choices"][0]["message"]["content"])
    #print(mol+": "+jsonized["choices"][0]["delta"]["content"])
    except json.decoder.JSONDecodeError or KeyError:
        print("Error:")
        print(jsonized)
        print("-----------------------------------")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='This is an AI api. use 35t for gpt-3.5-turbo, 4 for gpt-4.')
    parser.add_argument('param1', type=str, help='model selection')
    parser.add_argument('param2', type=str, help='message')
    args = parser.parse_args()
    main(args.param1, args.param2)
