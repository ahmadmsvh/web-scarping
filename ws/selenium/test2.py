from twocaptcha import TwoCaptcha

solver = TwoCaptcha('04123559dee20959d8d618467a406c9d')

config = {
            'server':           '2captcha.com',
            'apiKey':           '04123559dee20959d8d618467a406c9d',
            'softId':            123,
            'callback':         'https://your.site/result-receiver',
            'defaultTimeout':    120,
            'recaptchaTimeout':  600,
            'pollingInterval':   10,
        }
solver = TwoCaptcha(**config)

result = solver.geetest(gt='f1ab2cdefa3456789012345b6c78d90e',
  challenge='12345678abc90123d45678ef90123a456b',
  url='https://www.site.com/page/',
  param1=..., ...)
