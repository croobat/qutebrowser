# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html

import subprocess
import os
from qutebrowser.api import interceptor

# Load existing settings made via :set
config.load_autoconfig(True)

#  ╭───────╮
#  │ Pages │
#  ╰───────╯
c.url.default_page = 'https://www.google.com'
c.url.start_pages = 'https://www.google.com'
c.url.searchengines = {
    'DEFAULT': 'https://www.google.com/search?q={}',
    'yt': 'https://www.youtube.com/results?search_query={}',
    'am': 'https://www.amazon.com/s?k={}',
    'ml': 'https://listado.mercadolibre.com.mx/{}',
    'aw': 'https://wiki.archlinux.org/?search={}',
    'aur': 'https://archlinux.org/packages/?sort=&q={}',
    'pex': 'https://www.pexels.com/search/{}',
    'gh': 'https://github.com/search?q={}',
    'pirate': 'https://thepiratebay.org/search.php?q={}',
    'red': 'https://www.reddit.com/r/{}',
    'wiki': 'https://en.wikipedia.org/wiki/{}'
}

#  ╭─────────╮
#  │ Aliases │
#  ╰─────────╯
c.aliases = {
    'q': 'close',
    'qa': 'quit',
    'w': 'session-save',
    'wq': 'quit --save',
    'wqa': 'quit --save',
}

#  ╭──────────╮
#  │ Bindings │
#  ╰──────────╯
bindings = {
    # Faster
    '<Ctrl-j>': 'run-with-count 15 scroll down',
    '<Ctrl-k>': 'run-with-count 15 scroll up',
    # VIM like
    't': 'set-cmd-text -s : open -t',
    'xb': 'config-cycle statusbar.show always never',
    'xt': 'config-cycle tabs.show always never',
     'xx': 'config-cycle statusbar.show always never;; config-cycle tabs.show always never',
    'j': 'run-with-count 3 scroll down',
    'k': 'run-with-count 3 scroll up',
    'J': 'tab-prev',
    'K': 'tab-next',
    'ZQ': 'quit',
    'ZZ': 'quit --save',
    # Hints
    'yf': 'hint links yank',
    'yF': 'hint all yank',
    # Stylesheets
    ',,': 'greasemonkey-reload ;; reload',
    ',z': 'config-cycle content.user_stylesheets ~/.config/qutebrowser/solarized-everything-css/css/apprentice/apprentice-all-sites.css ""',
    ',x': 'config-cycle content.user_stylesheets ~/.config/qutebrowser/solarized-everything-css/css/darculized/darculized-all-sites.css ""',
    ',c': 'config-cycle content.user_stylesheets ~/.config/qutebrowser/solarized-everything-css/css/gruvbox/gruvbox-all-sites.css ""',
    ',v': 'config-cycle content.user_stylesheets ~/.config/qutebrowser/solarized-everything-css/css/solarized-dark/solarized-dark-all-sites.css ""',
    ',b': 'config-cycle content.user_stylesheets ~/.config/qutebrowser/solarized-everything-css/css/solarized-light/solarized-light-all-sites.css ""'
}
for binding in bindings:
    config.bind(binding, bindings[binding])

insertBindings = {
    "<Ctrl-h>": "fake-key <Backspace>",
    "<Ctrl-a>": "fake-key <Home>",
    "<Ctrl-e>": "fake-key <End>",
    "<Ctrl-b>": "fake-key <Left>",
    "<Mod1-b>": "fake-key <Ctrl-Left>",
    "<Ctrl-f>": "fake-key <Right>",
    "<Mod1-f>": "fake-key <Ctrl-Right>",
    "<Ctrl-p>": "fake-key <Up>",
    "<Ctrl-n>": "fake-key <Down>",
    "<Mod1-d>": "fake-key <Ctrl-Delete>",
    "<Ctrl-d>": "fake-key <Delete>",
    "<Ctrl-w>": "fake-key <Ctrl-Backspace>",
    "<Ctrl-u>": "fake-key <Shift-Home><Delete>",
    "<Ctrl-k>": "fake-key <Shift-End><Delete>"
}
for binding in insertBindings:
    config.bind(binding, insertBindings[binding], 'insert')

#  ╭─────────╮
#  │ Options │
#  ╰─────────╯
# Font
c.fonts.default_family = 'JetBrainsMono Nerd Font'
c.fonts.default_size = '10.5pt'

# Smooth scroll
c.scrolling.smooth = True

# Youtube autoplay
c.content.autoplay = False

# Downloads location
c.downloads.location.directory = '~/Downloads'
# Abort HTTP downloads from HTTPS pages
c.downloads.prevent_mixed_content = False

# Time (ms) between auto-saves (config, cookies, etc)
c.auto_save.interval = 15000

# Editor for editor-* commands
c.editor.command = ['nvim', '-f', '{file}', '-c', 'normal {line}G{column0}l']

# Status bar
c.statusbar.show = 'never'

# Tab bar
c.tabs.show = 'multiple'

#  ╭───────────────╮
#  │ ## Permisions │
#  ╰───────────────╯
# JavaScript
config.set('content.javascript.enabled', True, 'chrome-devtools://*')
config.set('content.javascript.enabled', True, 'devtools://*')
config.set('content.javascript.enabled', True, 'chrome://*/*')
config.set('content.javascript.enabled', True, 'qute://*/*')

# Cookies
config.set('content.cookies.accept', 'all', 'chrome-devtools://*')
config.set('content.cookies.accept', 'all', 'devtools://*')

# Load images
config.set('content.images', True, 'chrome-devtools://*')
config.set('content.images', True, 'devtools://*')

# Notifications
config.set('content.notifications.enabled', True, 'https://www.reddit.com')

# Accept_language header
config.set('content.headers.accept_language', '', 'https://matchmaker.krunker.io/*')

# TLS certificate
c.content.tls.certificate_errors = 'load-insecurely'

# User agents
config.set(
    'content.headers.user_agent',
    'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}',
    'https://web.whatsapp.com/'
)
config.set(
    'content.headers.user_agent',
    'Mozilla/5.0 ({os_info}; rv:90.0) Gecko/20100101 Firefox/90.0',
    'https://accounts.google.com/*'
)
config.set(
    'content.headers.user_agent',
    'Mozilla/5.0 ({os_info}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99 Safari/537.36',
    'https://*.slack.com/*'
)

#  ╭───────╮
#  │ Style │
#  ╰───────╯
# Dark mode
c.colors.webpage.preferred_color_scheme = 'dark'
config.set("colors.webpage.darkmode.enabled", True)

# Dracula color scheme
import dracula.draw
dracula.draw.blood(c)

# Custom styles
c.content.user_stylesheets =  ['~/.config/qutebrowser/styles.css']
