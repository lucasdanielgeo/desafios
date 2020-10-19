Encurtador de URLs
===========================

Seu serviço irá receber inicialmente como parâmetro uma URL que deverá ser encurtada seguindo as seguintes regras:

1. Mínimo de 5 e máximo de 10 caracteres.

2. Apenas letras e números. 

A url retornada deverá ser salva no banco de dados e possui prazo de validade (você poderá escolher quanto tempo) e ao receber uma url encurtada, deverá fazer o redirecionamento para a url salva no banco.

#### Exemplo ao encurtar
- Seu sitema recebe uma chamada para encurtar a url `backendbrasil.com.br` e retorna o seguinte json

``` 
{ 
  newUrl: "http://localhost:8081/abc123ab";
} 
```

#### Exemplo ao redirecionar
- Ao receber uma chamada para `http://localhost:8081/abc123ab` você irá retorna um redirecionamento para a url salva no banco (`backendbrasil.com.br`), caso não seja encontrada, retornar HTTP 404


# Short Url

A function that receives an URL and returns the following result: server URL + url hash

1. Define the object, with these attributes:
  - url
  - url_hash
  - short_url
  - creation_datetime
  - expiration_datetime

2. Define a function that makes a hash from the url input:
  - A hash must have between 5 and 10 characters, not including special characters, just letters;
  - After the hash is created, it must be concatenated with the server url, as a new route;

3. Determine an expiration time for the url, based on the DateTime the short_url was created;
  - set a function that deletes the Url instance, for this the expiration time will be 120 seconds after it was created the short URL;