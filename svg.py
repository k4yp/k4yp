# import requests
# import yaml

# USERNAME = 'k4yp'

# INFO_URL = 'https://api.github.com/users/' + USERNAME

# ALL_REPO_URL = INFO_URL + '/repos'

# ALL_LANG_URL = 'https://raw.githubusercontent.com/github/linguist/master/lib/linguist/languages.yml'

# all_langs = {}
# repo_names = []
# repo_langs = []

# repos_raw = requests.get(ALL_REPO_URL).json()

# for i in range (len(repos_raw)):
#     repo_names.append(repos_raw[i]['name'])

# for i in range(len(repo_names)):
#     repo_langs.append(requests.get('https://api.github.com/repos/' + USERNAME + '/' + repo_names[i] + '/languages').json())

# for i in range(len(repo_langs)):
#     for key, value in repo_langs[i].items():
#         if key in all_langs:
#             all_langs[key] += value
#         else:
#             all_langs[key] = value

# languages = {k: v for k, v in sorted(all_langs.items(), reverse=True, key=lambda item: item[1])}

# colors = []

# raw_lang_colors = requests.get(ALL_LANG_URL).text

# lang_colors = yaml.load_all(raw_lang_colors ,Loader=yaml.FullLoader)
# for lang_color in lang_colors:
#     for key, value in languages.items():
#         color_hex = lang_color[key]['color'].lstrip('#')
#         color_rgb = tuple(int(color_hex[i:i+2], 16) for i in (0, 2, 4))
#         colors.append(color_rgb)

languages = {'JavaScript': 82829, 'Python': 38668, 'Svelte': 17604, 'Jupyter Notebook': 13808, 'TeX': 11600, 'Rust': 10606, 'Vim Script': 7536, 'Shell': 3618, 'Lua': 2429, 'HTML': 1495, 'Haskell': 998, 'TypeScript': 242}
colors = [(241, 224, 90), (53, 114, 165), (255, 62, 0), (218, 91, 11), (61, 97, 23), (222, 165, 132), (25, 159, 75), (137, 224, 81), (0, 0, 128), (227, 76, 38), (94, 80, 134), (49, 120, 198)]

html = """
    <svg fill="none" viewBox="0 0 384 128" width="384" height="128" style='background-color: #0d1117' xmlns="http://www.w3.org/2000/svg">
    <foreignObject width="100%" height="100%">
    <div xmlns="http://www.w3.org/1999/xhtml">
    <div style="display: flex; flex-wrap: wrap;">
    <style>.lang{display: inline-block}.end{padding-right:16px}span{font-family:monospace;color:#FFFFFF;}</style>
    """

total_lines = sum(languages.values())

for i, (language, lines) in enumerate(languages.items()):
    percentage = (lines / total_lines) * 100
    rgb = colors[i]
    html += f'<div style="background-color: rgb{rgb}; width: {percentage}%; height: 10px;"></div>'

html += '</div>'

total = sum(languages.values())
for i, lang in enumerate(languages.keys()):
    percentage = (languages[lang] / total) * 100
    html += "<div class='lang'>"
    html += f"<span style='color:rgb{colors[i]}'>⬤</span>"
    html += f"<span> {lang} </span>"
    html += f"<span class='end'>{round(percentage, 2)}%</span>"
    html += "</div>"

html += "</div></foreignObject></svg>"

with open('card.svg', 'w', encoding="utf-8") as f:
    f.write(html)