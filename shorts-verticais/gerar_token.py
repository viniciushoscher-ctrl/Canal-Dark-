#!/usr/bin/env python3
"""Roda UMA vez no seu computador. Pede o Client ID e o Client Secret, abre o navegador
(entre com a conta do canal) e imprime o REFRESH TOKEN. Nada e salvo em arquivo.
pip install google-auth-oauthlib   |   python gerar_token.py"""
import getpass
from google_auth_oauthlib.flow import InstalledAppFlow
cid=input("Client ID: ").strip(); sec=getpass.getpass("Client Secret (nao aparece): ").strip()
cfg={"installed":{"client_id":cid,"client_secret":sec,"auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://oauth2.googleapis.com/token","redirect_uris":["http://localhost"]}}
c=InstalledAppFlow.from_client_config(cfg,["https://www.googleapis.com/auth/youtube.upload"]).run_local_server(port=0,access_type="offline",prompt="consent")
print("\nREFRESH TOKEN (cole direto no GitHub Secret YT_REFRESH_TOKEN, nao no chat):\n"+c.refresh_token)
