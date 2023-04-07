# EasyPasswordBackend

EasyPasswordBackend é um back-end rest Python desenvolvido do zero utilizando o frameword Django-Rest. Todos os end-points são autorizados e autenticados com a ajuda
da biblioteca Django-OAuth-Toolkit, a biblioteca de implementação do padrão OAuth2 recomendada pela própria  documentação do framework Django. Todas as informações
dos ussuarios e suas senhas são persistidos em um banco PostGresSQL hospedado com o site na plataforma Heroku, e pode ser
facilmente acessado através do admin próprio do framework Django. A API é extremamente simples e direta ao ponto, se resumindo pricipalmente a criação das senhas e a listagem das mesmas.

 Para ver uma implementação completa desse Back-End, por favor de uma olhada também no projeto [EasyPasswordFront](https://github.com/miratkd/EasyPasswordFront), um
 site Single-Page-Aplication desenvolvido usando o framework VueJs que consome todos os end-points desse projeto.
 
 Abaixo segue a documentação da API.
 
 ----
 
 ## Criar usuário
 
 Um end-point público para criar os usuários do sistema.
 
 **POST**:  https://easy-password.up.railway.app/account/
 
 **BODY**:
 {
 
    "user": {
        "username": O nome de usuário da conta, esse valor será usado como chave primário, por isso, caso um username já utilizado for passado, o end-poit retornara um erro informando que o username já foi utilizado. 
        "email": E-mail associado a aquela conta.
        "password": Senha de acesso para a conta que vai ser criada.
    }
    
 }
 
 **Exemplo 1**:
 {
 
    "user": { 
        "username": "lucas123", 
        "email": "lucas123@gmail.com", 
        "password": "13972684" 
    } 
 
 }
 
  **Exemplo 2**:
  {
  
      "user": { 
        "username": "joaoGamer", 
        "email": "joaogamer@gmail.com", 
        "password": "hightcode" 
      } 
  
  }
  
  ## Login
  
  End-point para receber um access token de uma certa conta.
  
  **POST:** https://easy-password.up.railway.app/o/token/
  
  **HEADER:** {
  
      "Content-Type": application/x-www-form-urlencoded
      
  }
  
  **BODY:**{
  
      "grant_type": " password " 
      "Username": Mesmo username passado na hora de criar a conta. 
      "Password": Mesmo password passado na hora de criar a conta. 
      "client_id": Chave de acesso do cliente. 
      "client_secret": senha de acesso do cliente. 
  
  }
  
  **Exemplo 1**:
 {
 
    "grant_type": " password " 
    "Username": "lucas123" 
    "Password": "13972684" 
    "client_id": "vErNybWh2TVRitDgec4jnx1ZdkkdHETvMHFK7xm” 
    "client_secret":"CFJ3Ovq0rqOMLWUWajwKtRdnlxF3LIFvSzlQJ5VsIBYILXDnnmA8kmoPRfGmInbp2Y6hvXITG8LaPrFPh9QqkHvgNF8I1sA2Q4X54ewqzyIM4uWSLpuxg3uHvNPsyned " 
 
 }
 
  **Exemplo 2**:
  {
  
      "grant_type": " password " 
      "Username": "joaoGamer" 
      "Password": "hightcode" 
      "client_id": "vErNybWh2TVRitDgec4jnx1ZdkkdHETvMHFK7xm” 
      "client_secret":"CFJ3Ovq0rqOMLWUWajwKtRdnlxF3LIFvSzlQJ5VsIBYILXDnnmA8kmoPRfGmInbp2Y6hvXITG8LaPrFPh9QqkHvgNF8I1sA2Q4X54ewqzyIM4uWSLpuxg3uHvNPsyned" 
  
  }
  
  **Resposta:** {
  
      "access_token": Token que deve ser passado nos endpoints autenticados. 
      "expires_in": duração do token em segundos. 
      "refresh_token": esse token pode ser usado para receber um novo access_token, uma vez que o primeiro já tenha expirado. 
      "scope": nível de permissão do access_token 
      "token_type": tipo do access_token 
  
  }
  
  **Exemplo de resposta:**{
  
      "access_token": "0DuJ7oPKhDRsoIbzpCeyY5dkXVKfkb" 
      "expires_in": 36000 (10 horas) 
      "refresh_token": "M2MmP3JuyYgWnqAqkshe3nM4rg3ANA" 
      "scope": "read write groups" 
      "token_type": "Bearer" 
  
  }
  
  ## Autenticação e autorização.
  
  Todos os end-points (com exceção do end-point de criar usuário e o de login) são privados, ou seja, é obrigatório passar um access_token para ter acesso aquele end-point. 

  O sistema de autorização e autenticação é uma implementação simples do protocolo OAuth2, feita através da biblioteca "Django OAuth Toolkit" 

  Para ser autenticado pelo servidor é preciso passar o seguinte parâmetro no header da request: 
  { 

    " Authorization ": tipo do token + access_token  

  } 

**Exemplo:**
{ 

    " Authorization ": "Bearer 0DuJ7oPKhDRsoIbzpCeyY5dkXVKfkb " 

}

## Informações da conta. 

Retorna informações da conta equivalente a aquele access_token. 

**GET**: https://easy-password.up.railway.app/account/me/ 

**HEADER**: 
{

    " Authorization ": tipo do token + access_token
    
}

**BODY**: {}

**RESPOSTA**:  
{

    "Id": o ID daquela conta.
    "User": { 
      "email": email cadastrado a aquela conta.
      "is_active": estado da conta.
      "username": nome de usuário associado a aquela conta. 
    }

}

**Exemplo de resposta**:
{

    "Id": 01 
    "User": { 
        "email": "lucas123@gmail.com", 
        "is_active": "true", 
        "username": "lucas123" 
    } 

}

## Salvar senha.

End-point para salvar uma nova senha a aquela conta. 

**PUT**: https://easy-password.up.railway.app/account/save_password/

**HEADER**: 
{

    " Authorization ": tipo do token + access_token

} 

**BODY**:
{

   "site": String representando o nome do site a qual aquela senha pertence.
   "password": String da senha que deve ser salva.

}

**Exemplo 1**:
{

    "site": "Kabum",
    "password": "1231231"

}
**Exemplo 2**:
{

    "site": "Youtube",
    "password": "13972684"

}

**RESPOSTA**: Objeto contendo site e senha criados.


## Listar senhas salvas.

End-point para listar todas as senhas associadas aquela conta. 

**GET**: https://easy-password.up.railway.app/account/passwords/

**HEADER**: 
{

    " Authorization ": tipo do token + access_token

} 


**RESPOSTA**: Lista de objetos contendo todas as senhas associadas a aquela conta.

**Exemplo de resposta**:
[

    {
        "site": "Youtube",
        "password": "13972684"
    },
    {
        "site": "Kabum",
        "password": "123123"
    },
    {
        "site": "Steam",
        "password": "741852963"
    }

]



