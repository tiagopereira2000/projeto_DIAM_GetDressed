# projeto_DIAM_GetDressed
## Modelos de Dados:
* ### Product
  * id
  * __name_product__ (String)
  * __stock__ (int)
  * __price__ (long)
  * tags (list[string])
* ### User
  * id
  * __name__ (string)
  * is_active (boolean)
* ### Cart
    * id
    * __user__ (User)
    * __product_list__ {{"product":x, amount:"y"},...}
    * __last_change__ (DateTime)
    * __is_active__ (boolean)
* ### Order
  * id
  * __user__ (User)
  * __payment_method__ (dropDownList)
  * __cart__ (Cart)



## Funcionalidades:
* __login__
* __logout__
* __register__
* __add_product2cart__
* __clean_cart__
* __add_product__
* __edit_product__
* __delete_product__
* __purchase__
* __search_product__
* __cart_view__
* __profile_view__


## Utilizadores e permissões:
* ### Anonimous
apenas pode observar os produtos, utilizar as views de pesquisar produto e fazer um carrinho temporário guardado em memória local até este fazer o registo.
* ### Client
Tem todas as funcionalidades ao seu dispor menos as de "add_product()" , "edit_product()" e "delete_product()".
Também não tem acesso a mexer na BD e criar novos utilizadores com permissões distintas.
* ### Admin
Tem acesso a toda a aplicação e gestão de dados desde a sua íntegra.


### Utilização de campos ManyToManyField:
> In[1]: chicken_teriyaki_sandwich = Sandwich.objects.create(name="Chicken Teriyaki Sandwich")
In[2]:bbq_sauce = Sauce.objects.create(name="Barbeque")
In[3]:mayo_sauce = Sauce.objects.create(name="Mayonnaise")
In[4]:chicken_teriyaki_sandwich.sauces.add(bbq_sauce)
In[5]:chicken_teriyaki_sandwich.sauces.add(mayo_sauce)
In[6]:chicken_teriyaki_sandwich.sauces.all()
Out[1]:<QuerySet [<Sauce: Barbeque>, <Sauce: Mayonnaise>]>


### Superuser:
username : admin
password : admin

### user2: Maria

### produtos:
tshirt básica, 15.5
casaco ganga, 50
