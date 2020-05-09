# Number Adder
[heading__top]:
  #number-adder
  "&#x2B06; Simple HTML input, JavaScript output number adder"


Simple HTML input, JavaScript output number adder


## [![Byte size of Number Adder][badge__gh_pages__number_adder__source_code]][number_adder__gh_pages__source_code] [![Open Issues][badge__issues__number_adder]][issues__number_adder] [![Open Pull Requests][badge__pull_requests__number_adder]][pull_requests__number_adder] [![Latest commits][badge__commits__number_adder__gh_pages]][commits__number_adder__gh_pages] [![number-adder Demos][badge__gh_pages__number_adder]][gh_pages__number_adder]


------


- [:arrow_up: Top of Document][heading__top]

- [:building_construction: Requirements][heading__requirements]

- [:zap: Quick Start][heading__quick_start]

  - [:trident: Fork][heading__fork]
  - [&#x1F9F0; Usage][heading__usage]

- [&#x1F5D2; Notes][heading__notes]

- [:card_index: Attribution][heading__attribution]

- [:balance_scale: Licensing][heading__license]


------



## Requirements
[heading__requirements]:
  #requirements
  "&#x1F3D7; Prerequisites and/or dependencies that this project needs to function properly"


A web browser, and optionally Python installed for running a local web-server.


___


## Quick Start
[heading__quick_start]:
  #quick-start
  "&#9889; Perhaps as easy as one, 2.0,..."


Clone this project...


**Linux/MacOS**


```Bash
mkdir -vp ~/git/hub/web-dev-examples

cd ~/git/hub/web-dev-examples

git clone git@github.com:web-dev-examples/number-adder.git
```


**Windows**


```Batch
set _organization_directory="%HOMEDRIVE%%HOMEPATH%\git\hub\web-dev-examples"

if not exists %_organization_directory (
  md %_organization_directory
)

CD /D %_organization_directory

git clone git@github.com:web-dev-examples/number-adder.git
```


------


### Fork
[heading__fork]:
  #fork
  "&#x1F531; Fork this repository to track customizations"


- [Fork](https://github.com/web-dev-examples/number-adder/fork) this repository to an Account or Organization that you have write permissions to.

- Add the fork URL to the list of Git remotes...


**Linux/MacOS**


```Bash
_account="your-name"

git remote add fork "git@github.com:${_account}/number-adder.git"
```


**Windows**


```Batch
set _account="your-name"

git remote add fork "git@github.com:%_account%/number-adder.git"
```


- Public demo of Fork URL syntax `https://<account-name>.github.io/number-adder`


------


### Usage
[heading__usage]:
  #usage
  "&#x1F9F0;"


- Run `server.py` script...


```Bash
./server.py
```


- Navigate to `localhost:8080`

- Edit an `index` file and save changes

- Refresh browser to view changes

- Commit the changes that are worth saving...


```Bash
git add index.*

git commit -m 'Fixes something or adds nifty feature'
```


- Push changes to your fork...


```Bash
git push fork number-adder
```


___


## Notes
[heading__notes]:
  #notes
  "&#x1F5D2; Additional things to keep in mind when developing"


This repository is intended to be a simple yet fully functioning example of HTML, CSS, and JavaScript web development. Pull Requests that fix bugs are very welcome, however, please keep in mind that the goal of this repository is to be accessible to all developer levels.


___


## Attribution
[heading__attribution]:
  #attribution
  "&#x1F4C7; Resources that where helpful in building this project so far."


- [GitHub -- `github-utilities/make-readme`](https://github.com/github-utilities/make-readme)

- [Python Docs -- `http.server`](https://docs.python.org/3/library/http.server.html)

- [StackOverflow -- how to run a `http.server` which serves a specific path?](https://stackoverflow.com/questions/39801718/)


___


## License
[heading__license]:
  #license
  "&#x2696; Legal side of Open Source"


```
Documentation for simple HTML input, JavaScript output number adder
Copyright (C) 2020 S0AndS0

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

```


For further details review full length version of [AGPL-3.0][branch__current__license] License.



[branch__current__license]:
  /LICENSE
  "&#x2696; Full length version of AGPL-3.0 License"


[badge__commits__number_adder__gh_pages]:
  https://img.shields.io/github/last-commit/web-dev-examples/number-adder/gh-pages.svg

[commits__number_adder__gh_pages]:
  https://github.com/web-dev-examples/number-adder/commits/gh-pages
  "&#x1F4DD; History of changes on this branch"


[number_adder__community]:
  https://github.com/web-dev-examples/number-adder/community
  "&#x1F331; Dedicated to functioning code"

[number_adder__gh_pages]:
  https://github.com/web-dev-examples/number-adder/tree/
  "Source code examples hosted thanks to GitHub Pages!"

[badge__gh_pages__number_adder]:
  https://img.shields.io/website/https/web-dev-examples.github.io/number-adder/index.html.svg?down_color=darkorange&down_message=Offline&label=Demo&logo=Demo%20Site&up_color=success&up_message=Online

[gh_pages__number_adder]:
  https://web-dev-examples.github.io/number-adder/index.html
  "&#x1F52C; Check the example collection tests"

[issues__number_adder]:
  https://github.com/web-dev-examples/number-adder/issues
  "&#x2622; Search for and _bump_ existing issues or open new issues for project maintainer to address."

[pull_requests__number_adder]:
  https://github.com/web-dev-examples/number-adder/pulls
  "&#x1F3D7; Pull Request friendly, though please check the Community guidelines"

[number_adder__gh_pages__source_code]:
  https://github.com/web-dev-examples/number-adder/
  "&#x2328; Project source!"

[badge__issues__number_adder]:
  https://img.shields.io/github/issues/web-dev-examples/number-adder.svg

[badge__pull_requests__number_adder]:
  https://img.shields.io/github/issues-pr/web-dev-examples/number-adder.svg

[badge__gh_pages__number_adder__source_code]:
  https://img.shields.io/github/repo-size/web-dev-examples/number-adder
