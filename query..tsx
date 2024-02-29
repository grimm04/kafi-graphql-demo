

  mutation{
    auth(username:"grimm",password:"secret"){
      accessToken
      refreshToken
    }
  }
  {
  "data": {
    "auth": {
      "accessToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzMTQ0Nzc4NSwianRpIjoiOTIxNTUyNjktZDhkYi00NDQwLWE4MmQtZTIwNWM3NzUwN2QyIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImdyaW1tIiwibmJmIjoxNjMxNDQ3Nzg1LCJleHAiOjE2MzE1MzQxODV9.Vs4THij6a-OHg6SPrxqDNVYuHTxe7h0AhQiqmpEUt2s",
      "refreshToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzMTQ0Nzc4NSwianRpIjoiNGQ1MmU3MzYtZTM1OC00NTE1LTkwY2YtZmViMzA5ZThhZmZkIiwidHlwZSI6InJlZnJlc2giLCJzdWIiOiJncmltbSIsIm5iZiI6MTYzMTQ0Nzc4NSwiZXhwIjoxNjM0MDM5Nzg1fQ.jLc9jHJar_syM_6X-PDpl2_N___ohB2zWza_EwAGGf0"
    }
  }
}
mutation{
  createProduk(input:{nama:"Produk 1",deskripsi:"Produk1"}){
    ok
    produk{
      nama
      deskripsi
    }
  }
}

mutation{
  updateProduk(input:{id:"UHJvZHVrOjI=",nama:"Produk 2"}){
    ok
    produk{
      nama
      id
    }
  }
}

mutation{
  deleteProduk(id:"UHJvZHVrOjE="){
    ok
    msg
  }
}

// paket
{
  paketById(paketId:1){
    id
    nama
    deskripsi
  }
}
mutation{
  createPaket(input:{nama:"Gold",deskripsi:"Gold"}){
    ok
    msg
    paket{
      id
      nama
    }
  }
}

mutation{
  updatePaket(input:{id:"UGFrZXQ6Mg==",nama:"Silver1",deskripsi:"Silver1"}){
    ok
    paket{
      id
      nama
    }
  }
}

mutation{
  deletePaket(id:"UGFrZXQ6Mg=="){
    ok
    msg
  }
}



mutation{
  createUser(input:{fullname:"aaasi",email:"asi@gmail.com",username:"asi",password:"asi"}){
    ok
    user{
      fullname
      username
    }
  }
}



{
  allUsers(filters:{createdAtRange:{begin:"2021-09-04T00:00:00",end:"2021-09-10T00:00:00"}}){
    totalCount
    edges{
      node{
        id
        fullname
        email
        username
        createdAt
      }
    }
  }
}


mutation createSlider($input: SliderInput!){
  createSlider(input:$input){
    ok
    slider{
      title
      description
      active
      id
      image
    }     
  }
}

mutation createPortofolio($input : PortofolioInput!){
  createPortofolio(input: $input){
    portofolio{
      id
      nama
      gambar
      kusionerId
    }
  }
}

VXNlck5vZGU6MQ==

$2b$12$MhQ2vQ2Vgqu1IIWEExsg7eVLZDfSCEtUgqL5vrYk0zsrnGkbpyVdW