# Pony skin retriever
This is a Python implementation of [this server](https://github.com/niteru/PonySkinRetriever/) (Node starts too long)

## How to use it
To fetch a skin from Mine Little Pony mod server, just go to `https://ponyskins.herokuapp.com/<nickname>` where `<nickname>` must be replaced with your nickname

Also supports cross-domain requests

For AJAX requests, there is also `X-Nickname` header available if profile for provided nickname is found (may be used for showing correct register of nickname letters)
