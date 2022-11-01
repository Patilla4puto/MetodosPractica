<TeXmacs|1.99.18>

<style|<tuple|generic|spanish>>

<\body>
  <section|Raíces \ \ de \ \ funciones \ \ no \ \ lineales \ \ - \ \ Parte
  \ \ 3>

  <subsection|Presentacion de la covergencia del metodo Newton-Rapshon>

  En este apartado queremos ilustrar como converge el metodo Newton-Rapshon.
  Para ello, primero recordamos que se denominan a K constante y a k orden de
  convergencia, a los números tales que:

  <\equation*>
    lim<rsub|n\<rightarrow\>\<infty\>><frac|<around*|\||x<rsup|n+1><rsub|0>-x<rsub|0>|\|>|<around*|\||x<rsup|n><rsub|0>-x<rsub|0>|\|><rsup|k>>=K
  </equation*>

  Es conocido que en el caso de Newton-Rapshon el orden de convergencia es
  cuadrático y su constante de convergencia tiene valor:

  <\equation>
    K=<around*|\||<frac|1f<rsup|<rprime|''>><around*|(|x<rsub|0>|)>|2f<rsup|<rprime|'>><around*|(|x<rsub|0>|)>>|\|><space|2em><text|En
    donde <math|f> es la funcion analizada y <math|x<rsub|0>> es la raiz
    obtenida>
  </equation>

  No obstante, no conocemos como se comporta esta K, según el orden de
  convergencia. Por ello, para ilustrar dicho comportamiento realizaremos un
  ejemplo practica donde anotaremos en una tabla los valores de K y
  <math|E<rsub|n>> (error entre la estimación y la raiz real), según el
  numero de iteraciones (n) y según el valor del orden de convergencia.

  <subsection|Convergencia para f(x) = <math|x<rsup|3>-3x+2> y
  <math|x<rsub|0>=-3>>

  Para analizar la convergencia de f(x), tomamos una tolerancia de
  <math|\<varepsilon\>=1\<ast\>10<rsup|-6>> y modificamos el programa inicial
  del metodo de Newton-Rapshon para que admitiera un nuevo parámetro que le
  indicase la iteración en la que debía detenerse. Además, creamos una
  función auxilliar que encapsula al metodo de Newton-Rapshon, cuyo objetivo
  es el de devolver el valor final del metodo para una iteración dado, asi
  como el error cometido en esa iteración y un array con los K para los
  ordenes de convergencia k=1, k=2 y k=3. Que tiene el siguiente aspecto:

  <with|prog-scripts|python|<\code>
    def conv_NewtonRapshon(f,x_m,epsilon,limit,x_0):<next-line><next-line>
    \ \ \ if(limit\<gtr\>0):<next-line> \ \ \ \ \ \ \ #SI limit NO ES
    0,APLICAMOS NEWTON_RAPSON HASTA LA ITERACION limit(n)<next-line>
    \ \ \ \ \ \ \ aux=metodo_NewtonRaphson(f,x_m,epsilon,limit=limit)<next-line>
    \ \ \ \ \ \ \ """ \ \ \ \ \ \ \ 

    \ \ \ \ \ \ \ \ Haciendo limit =limit, basicamente estamos especificando
    que la variable<next-line> \ \ \ \ \ \ \ limit independientemente de
    donde se declarese en la cabecera de la\ 

    \ \ \ \ \ \ \ \ funcion metodo_NewtonRaphson tenga valor limit<next-line>
    \ \ \ \ \ \ \ ``""<next-line> \ \ \ else:<next-line> \ \ \ \ \ \ \ # SI
    limit ES CERO, ENTONCES X_N=x_m<next-line>
    \ \ \ \ \ \ \ aux=[x_m]<next-line> \ \ \ #VALOR DEVUELTO POR
    NEWTON_RAPSON EN LA ITERACION limit(n+1)<next-line> \ \ \ aux1 =
    metodo_NewtonRaphson(f,x_m,epsilon,limit=limit+1)<next-line><next-line>
    \ \ \ #ERRORES E_n y E_n+1<next-line> \ \ \ e_n = aux[0]-x_0<next-line>
    \ \ \ e_n1= aux1[0]-x_0<next-line><next-line> \ \ \ k=[]<next-line>
    \ \ \ #ALMACENAMOS LOS K SEGUN la k<next-line> \ \ \ for i in
    range(1,4):<next-line> \ \ \ \ \ \ \ k.append(abs(e_n1)/(abs(e_n)**i))<next-line>
    \ \ \ return aux[0],e_n,k
  </code>>

  Tras esto, implementamos un bucle en el se mostraban los resultados de la
  aplicacion de este metodo para valores de limit entre 0 y 4 (iteracion a
  partir de la cual el metodo converge por lo que los siguientes resultados
  carecerián de significado), donde obtuvimos los resultados que se reflejan
  en la siguiente tabla:

  <\big-table|<tabular|<tformat|<table|<row|<cell|<wide-tabular|<tformat|<cwith|2|-1|1|1|cell-valign|c>|<cwith|2|-1|1|1|cell-halign|c>|<twith|table-rborder|4>|<cwith|2|-1|1|1|cell-lborder|1ln>|<cwith|2|2|1|1|cell-hyphen|n>|<cwith|2|2|1|1|cell-bborder|0ln>|<cwith|3|3|1|1|cell-tborder|0ln>|<cwith|2|2|1|1|cell-lborder|1ln>|<cwith|6|6|1|1|cell-tborder|0ln>|<cwith|5|5|1|1|cell-bborder|0ln>|<cwith|6|6|1|1|cell-bborder|1ln>|<cwith|6|6|1|1|cell-lborder|1ln>|<cwith|2|-1|2|2|cell-lborder|1ln>|<cwith|2|-1|1|1|cell-rborder|1ln>|<cwith|2|-1|3|3|cell-lborder|1ln>|<cwith|2|-1|2|2|cell-rborder|1ln>|<cwith|2|-1|4|4|cell-lborder|1ln>|<cwith|2|-1|3|3|cell-rborder|1ln>|<cwith|2|-1|5|5|cell-lborder|1ln>|<cwith|2|-1|4|4|cell-rborder|1ln>|<cwith|2|-1|6|6|cell-lborder|1ln>|<cwith|2|-1|5|5|cell-rborder|1ln>|<cwith|2|-1|6|6|cell-rborder|1ln>|<cwith|1|1|1|-1|cell-tborder|1ln>|<cwith|1|1|1|-1|cell-bborder|1ln>|<cwith|2|2|1|-1|cell-tborder|1ln>|<cwith|1|1|1|1|cell-lborder|1ln>|<cwith|6|6|2|-1|cell-tborder|0ln>|<cwith|5|5|2|-1|cell-bborder|0ln>|<cwith|6|6|2|-1|cell-bborder|1ln>|<cwith|6|6|2|2|cell-lborder|1ln>|<cwith|6|6|1|1|cell-rborder|1ln>|<cwith|6|6|6|6|cell-rborder|1ln>|<cwith|1|1|2|-1|cell-tborder|1ln>|<cwith|1|1|2|-1|cell-bborder|1ln>|<cwith|2|2|2|-1|cell-tborder|1ln>|<cwith|1|1|2|2|cell-lborder|1ln>|<cwith|1|1|1|1|cell-rborder|1ln>|<cwith|1|1|6|6|cell-tborder|1ln>|<cwith|1|1|6|6|cell-bborder|1ln>|<cwith|2|2|6|6|cell-tborder|1ln>|<cwith|1|1|6|6|cell-rborder|1ln>|<cwith|1|1|5|5|cell-tborder|1ln>|<cwith|1|1|5|5|cell-bborder|1ln>|<cwith|2|2|5|5|cell-tborder|1ln>|<cwith|1|1|5|5|cell-rborder|1ln>|<cwith|1|1|6|6|cell-lborder|1ln>|<cwith|1|1|4|4|cell-tborder|1ln>|<cwith|1|1|4|4|cell-bborder|1ln>|<cwith|2|2|4|4|cell-tborder|1ln>|<cwith|1|1|4|4|cell-rborder|1ln>|<cwith|1|1|5|5|cell-lborder|1ln>|<cwith|1|1|3|3|cell-tborder|1ln>|<cwith|1|1|3|3|cell-bborder|1ln>|<cwith|2|2|3|3|cell-tborder|1ln>|<cwith|1|1|3|3|cell-lborder|1ln>|<cwith|1|1|2|2|cell-rborder|1ln>|<cwith|1|1|3|3|cell-rborder|1ln>|<cwith|1|1|4|4|cell-lborder|1ln>|<cwith|1|-1|2|-1|cell-background|>|<cwith|1|-1|2|-1|cell-halign|c>|<table|<row|<\cell>
    \;
  </cell>|<\cell>
    <math|x<rsup|n><rsub|0>>
  </cell>|<\cell>
    <math|E<rsub|n>>
  </cell>|<\cell>
    <\math>
      <around*|\||E<rsub|n+1>|\|> <frac*||><around*|\||E<rsub|n+1>|\|><rsup|k>
    </math>

    k = 1
  </cell>|<\cell>
    <\math>
      <around*|\||E<rsub|n+1>|\|> <frac*||><around*|\||E<rsub|n+1>|\|><rsup|k>
    </math>

    k = 2
  </cell>|<\cell>
    <\math>
      <around*|\||E<rsub|n+1>|\|> <frac*||><around*|\||E<rsub|n+1>|\|><rsup|k>
    </math>

    k = 3
  </cell>>|<row|<cell|n= 0>|<\cell>
    -3
  </cell>|<\cell>
    -1
  </cell>|<\cell>
    0.055555
  </cell>|<\cell>
    0.055555
  </cell>|<\cell>
    0.055555
  </cell>>|<row|<\cell>
    1
  </cell>|<\cell>
    -2.055555
  </cell>|<\cell>
    -0.055555
  </cell>|<\cell>
    0.035087
  </cell>|<\cell>
    0.631578
  </cell>|<\cell>
    11.36842
  </cell>>|<row|<\cell>
    2
  </cell>|<\cell>
    -2.001949
  </cell>|<\cell>
    -0.001949
  </cell>|<\cell>
    0.001297
  </cell>|<\cell>
    0.665369
  </cell>|<\cell>
    341.334630
  </cell>>|<row|<\cell>
    3
  </cell>|<\cell>
    -2.000002
  </cell>|<\cell>
    -0.000002
  </cell>|<\cell>
    0.000001
  </cell>|<\cell>
    0.666659
  </cell>|<\cell>
    263679.089
  </cell>>|<row|<\cell>
    4
  </cell>|<\cell>
    -2.000000
  </cell>|<\cell>
    <math|-4.2614*\<ast\>10<rsup|-12>>
  </cell>|<\cell>
    0
  </cell>|<\cell>
    0
  </cell>|<\cell>
    0
  </cell>>>>>>>>>>>
    \;
  </big-table>

  De aquí podemos observar varias cosas, la primera es que la convergencia
  del metodo se da en n=5 como indicamos antes lo cual explica porque las
  contantes de convergencia acaban siendo 0 para n=4.\ 

  Por otro lado, podemos observar que mientras la K para el orden de
  convergencia 3 parece divergir, la de los ordenes 1 y 2 parece
  estabilizarse en los valores 0 y <math|0.<wide|6|^>>. Por tanto podemos
  asegurar que el orden de convergencia es 2 ya que es el mayor orden que
  obtenemos y que la constante de convergencia es algo cercano a
  <math|0.<wide|6|^>>, lo cual podemos verificar haciendo uso de la formula
  (1), en donde tendriamos:

  <\wide-tabular>
    <tformat|<table|<row|<\cell>
      <math|f<rprime|'>(x)=3x<rsup|2>-3><space|2em>,<space|2em><math|f<rprime|''>(x)=6x<rsup|>><space|3em>,<space|3em><math|x<rsub|0>=-2>

      por lo que :\ 

      <\equation*>
        K=<around*|\||<frac|1\<ast\>-12|2\<ast\><around*|(|12-3|)>>|\|>=<around*|\||<frac|1\<ast\>-4|2\<ast\>3>|\|>=<frac|2|3>=0.<wide|6|^>
      </equation*>
    </cell>>>>
  </wide-tabular>

  Con lo que no solo comprobamos de manera analítica que el orden de
  convergencia del metodo es de orden 2, si no que tambien vemos que la
  formula que conocemos para obtener la constante de convergencia se cumple.

  <section|Resolución numérica de sistemas lineales>

  En este apartado estamos interesados en la resolución de sistemas de
  ecuaciones lineales. En este caso centramos nuestra atención en los
  algoritmo de Gauss-Seidel y en el de Jacobi los cuales descibiremos a
  continuación.

  Para ello vamos a tratar con sistemas de ecuaciones donde se considerará la
  siguiente notación.

  <\notation>
    \;

    Dado un sistema de ecuaciones Ax=b denotaremos los elementos de A como
    <math|a <rsub|kj>> donde la k representa la fila y j la columna,
    <math|x<rsub|j><rsup|i>> donde i es la iteración y j el elemento del
    vector y <math|b<rsub|j>> donde j es el elemento del vetor.
  </notation>

  <subsection|Descripción e implementación de los algoritmos>

  Los dos algoritmos que se van a implementar, pertenencen a la categoría de
  algoritmos iterativos, este tipo de algoritmos destacan por su simplicidad
  y por estar adaptados a sistemas grandes con matrices dispersas.

  Además, estos algoritmos resultan ser convergentes si se da la condición de
  que son diagonalmente dominantes o lo que es lo mismo, si:

  <\equation*>
    <around*|\||a<rsub|ii>|\|>\<gtr\><below|<big|sum><rsub|j=1><rsup|n>|j\<neq\>i><around*|\||a<rsub|ij>|\|>
  </equation*>

  La condición de convergencia de ambos algoritmos es identica y se basa en
  comprobar elemento a elemento el valor absoluto de la resta de la solución
  en la iteración anteriror con la solución en la iteración siguiente. De tal
  forma que si que en todos los elementos de los vectores se cumple que el
  valor absoluto de las restas es menor a epsilon entonces el algoritmo habrá
  alcanzado la condición de parada.

  Este comprobación fue implementada en un metodo, la cual devuelve un
  booleano a True si se da la condición de parada. Este metodo se presenta a
  continuación:

  <with|prog-scripts|python|>

  <with|prog-scripts|python|<\code>
    <code|def convergencia(e,x_k,x_k1):<next-line> \ \ \ i=0<next-line>
    \ \ \ conv = True<next-line> \ \ \ while(i\<less\>len(x_k) and
    conv):<next-line> \ \ \ \ \ \ \ if(abs(x_k[i]-x_k1[i])\<gtr\>
    e):<next-line> \ \ \ \ \ \ \ \ \ \ \ conv = False<next-line>
    \ \ \ \ \ \ \ i+=1<next-line> \ \ \ return conv>
  </code>>

  tras esto se procedió a la implementación de los dos algoritmos.

  <paragraph|Gauss-Seidel>

  El metodo Gauss-Seidel se retro alimenta puesto que los elementos del
  vector x se van actualizando no solo segun los elementos x de la iteración
  anterior si no que tambien con los elementos x ya calculados de esta
  iteración, la forma en la que se lleva a cabo esto es siguiendo la
  siguiente fórmula:

  <\equation>
    x<rsup|i><rsub|j>=<frac|b<rsub|j>-<below|<above|<big|sum>|j-1>|k=1>a<rsub|jk>\<ast\>x<rsup|i><rsub|k>
    -<below|<above|<big|sum>|n>|k=i+1>a<rsub|jk>\<ast\>x<rsup|i-1><rsub|k>
    |a<rsub|jj>>
  </equation>

  Dicha formula y el algoritmo como tal fueron implementados en una función
  como se muestra a continuación:

  <with|prog-scripts|python|<code|def Gauss_Seidel(A,b,x_0,e):<next-line>
  \ \ \ #De momento \ es igual a jacobi<next-line> \ \ \ x_k1 =
  np.copy(x_0)+2*e<next-line> \ \ \ k=1<next-line> \ \ \ x_k=
  np.copy(x_0)<next-line> \ \ \ while(not
  convergencia(e,x_k1,x_k)):<next-line><next-line>
  \ \ \ \ \ \ \ x_k1=np.copy(x_k)<next-line><next-line> \ \ \ \ \ \ \ for i
  in range(len(x_0)):<next-line> \ \ \ \ \ \ \ \ \ \ \ aux = b[i]<next-line>
  \ \ \ \ \ \ \ \ \ \ \ for j \ in range(len(x_0)):<next-line>
  \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ if(j != i):<next-line>
  \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ aux -=A[i,j]*x_k[j]#En vez de usar el
  vector de la iteracion anterior<next-line>
  \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ #usamos los valores del de la
  itearacion actual que depende de la fila<next-line>
  \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ # en la que estemos habran sido ya
  modificados<next-line> \ \ \ \ \ \ \ \ \ \ \ x_k[i]=aux/A[i,i]<next-line>
  \ \ \ \ \ \ \ print(k,":",x_k)<next-line>
  \ \ \ \ \ \ \ k+=1<next-line><next-line> \ \ \ return x_k>>

  En donde se puede observar que el algoritmo usa para implementar la fórmula
  (2) un vector que se inicializa con los valores de la iteración anterior y
  que se actualiza tras realizar el calculo sobre uno de sus elementos, por
  lo que acaba conteniendo las soluciones de esta iteración y de la anterior.

  <paragraph|Jacobi>

  Este otro metodo, es practicamente idéntico al de Gauss-Seidel, con la
  peculiaridad de que solo usa los valores de la iteración actual sin
  importar que elemento del vector x se este actualizando. Por ello, la
  fromula para actualizar los elementos de x queda simplificada a :

  <\equation>
    x<rsup|i><rsub|j>=<frac|b<rsub|j>-<below|<below|<above|<big|sum>|n>|k=1>|k\<neq\>j>a<rsub|jk>\<ast\>x<rsup|i-1><rsub|k>
    |a<rsub|jj>>
  </equation>

  De esta forma el algoritmo que implementa este metodo es practicamente una
  copia del de Gauss-Seidel pero en vez de usar el mismo vector que
  actualizamos para realizar los calculos de los elementos de x para esta
  iteración, usaremos un vector copia del de la iteración anterior pero sin
  actualizarlo, quedando con el siguiente aspecto:

  <with|prog-scripts|python|<\code>
    def jacobi(A,b,x_0,e):<next-line> \ \ \ x_k1 = np.copy(x_0) + 2*e
    #Copiamos el vector x_0 y sumamos a todos sus elementos<next-line>
    \ \ \ #2e para que el bucle se ejecute al menos una vez (python no tiene
    repeat until)<next-line> \ \ \ x_k = np.copy(x_0) #Se copia un vector con
    los mismos elementos<next-line> \ \ \ k=1 #Variable que alamcena el
    numero de la iteración<next-line><next-line> \ \ \ while (not
    convergencia(e, x_k1, x_k)):#Mientras no haya convergencia<next-line>
    \ \ \ \ \ \ \ x_k1 = np.copy(x_k)<next-line> \ \ \ \ \ \ \ for i in
    range(len(x_0)): # recorrido de las filas<next-line>
    \ \ \ \ \ \ \ \ \ \ \ aux = b[i]\ 

    \ \ \ \ \ \ \ \ \ \ \ \ for j in range(len(x_0)): # recorrido en
    columnas<next-line> \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ if (j != i):<next-line>
    \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ aux -= A[i, j] * x_k1[j]
    \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ 

    \ \ \ \ \ \ \ \ \ \ \ \ x_k[i] = aux/A[i,i] #Dividimos por el elemento de
    la diagonal<next-line> \ \ \ \ \ \ \ print(k,":",x_k)<next-line>
    \ \ \ \ \ \ \ k+=1<next-line> \ \ \ return x_k
  </code>>

  <subsection|Problemas planteados y su resolución>

  Para comprobar el fucnionamiento de ambos algoritmos, dos problemas fueron
  planteados. En esta sección enunciaremos dichos problemas y veremos un par
  de pasos iteratiivos asi como las soluciones que ambos metodos arrojaron.

  \;

  <\wide-tabular>
    <tformat|<twith|table-lsep|1>|<twith|table-hyphen|y>|<cwith|1|1|1|1|cell-row-span|2>|<cwith|1|1|1|1|cell-col-span|1>|<cwith|2|2|1|1|cell-halign|r>|<table|<row|<\cell>
      <math|>
    </cell>|<\cell>
      <math|3x<rsub|1>-0.1x<rsub|2>-0.2x<rsub|3>=7,85>
    </cell>>|<row|<\cell>
      1)
    </cell>|<\cell>
      <math|0.1x<rsub|1>+7x<rsub|2>-0.3x<rsub|3>=-19.3>

      <math|0.3x<rsub|1>-0.2x<rsub|2>+10x<rsub|3>=71.4>
    </cell>>>>
  </wide-tabular>

  En este sistema se pedia obtener una solución partiendo el vector inicial 0
  y una toleracia variable, en este caso obtamos por una tolerancia
  <math|\<varepsilon\>=0.1> y sabiendo que los resultados eran
  <math|x<rsub|1>=3;x<rsub|2>=-2.5;x<rsub|3>=7>. Obtuvimos los resultados
  recogidos en la siguiente tabla

  \;

  <\big-table|<tabular|<tformat|<table|<row|<cell|<tabular|<tformat|<cwith|2|4|1|1|cell-valign|c>|<cwith|2|4|1|1|cell-halign|c>|<cwith|2|4|1|1|cell-lborder|1ln>|<cwith|2|2|1|1|cell-hyphen|n>|<cwith|2|2|1|1|cell-lborder|1ln>|<cwith|2|4|2|2|cell-lborder|1ln>|<cwith|2|4|1|1|cell-rborder|1ln>|<cwith|2|4|3|3|cell-lborder|1ln>|<cwith|2|4|2|2|cell-rborder|1ln>|<cwith|2|4|4|4|cell-lborder|1ln>|<cwith|2|4|3|3|cell-rborder|1ln>|<cwith|2|4|4|4|cell-rborder|1ln>|<cwith|1|1|1|5|cell-tborder|1ln>|<cwith|1|1|1|5|cell-bborder|1ln>|<cwith|2|2|1|5|cell-tborder|1ln>|<cwith|1|1|1|1|cell-lborder|1ln>|<cwith|1|1|2|5|cell-tborder|1ln>|<cwith|1|1|2|5|cell-bborder|1ln>|<cwith|2|2|2|5|cell-tborder|1ln>|<cwith|1|1|2|2|cell-lborder|1ln>|<cwith|1|1|1|1|cell-rborder|1ln>|<cwith|1|1|4|4|cell-tborder|1ln>|<cwith|1|1|4|4|cell-bborder|1ln>|<cwith|2|2|4|4|cell-tborder|1ln>|<cwith|1|1|4|4|cell-rborder|1ln>|<cwith|1|1|3|3|cell-tborder|1ln>|<cwith|1|1|3|3|cell-bborder|1ln>|<cwith|2|2|3|3|cell-tborder|1ln>|<cwith|1|1|3|3|cell-lborder|1ln>|<cwith|1|1|2|2|cell-rborder|1ln>|<cwith|1|1|3|3|cell-rborder|1ln>|<cwith|1|1|4|4|cell-lborder|1ln>|<cwith|1|4|2|5|cell-background|>|<cwith|1|4|2|5|cell-halign|c>|<cwith|3|3|1|-1|cell-tborder|1ln>|<cwith|2|2|1|-1|cell-bborder|1ln>|<cwith|3|3|1|-1|cell-bborder|1ln>|<cwith|3|3|1|1|cell-lborder|1ln>|<cwith|3|3|4|4|cell-rborder|1ln>|<table|<row|<cell|iteración>|<cell|<math|x<rsup|1>>>|<cell|<math|x<rsup|2>>>|<cell|<math|<rsup|>>Final>>|<row|<cell|Gauss-Seidel>|<cell|[
  2.6166 -2.7945 \ 7.0056]>|<cell|[ 2.9905 -2.4996
  \ 7.0002]>|<cell|<math|x<rsup|3>=>[ 3.00003 \ -2.4999
  \ 6.999]>>|<row|<cell|Jacobi>|<cell|[ 2.6166 -2.7571 \ 7.14 ]>|<cell|[
  3.0007 \ -2.4885 \ 7.0063]>|<cell|<math|x<rsup|3>=>[ 3.0008 -2.4997
  \ 7.0002]>>>>>>>>>>>
    \;
  </big-table>

  <\wide-tabular>
    <tformat|<twith|table-lsep|1>|<twith|table-hyphen|y>|<cwith|1|1|1|1|cell-row-span|2>|<cwith|1|1|1|1|cell-col-span|1>|<cwith|2|2|1|1|cell-halign|r>|<table|<row|<\cell>
      <math|>
    </cell>|<\cell>
      <math|5x<rsub|1>+2x<rsub|2>-x<rsub|3>+x<rsub|4>=12>
    </cell>>|<row|<\cell>
      2)\ 

      \;
    </cell>|<\cell>
      <math|x<rsub|1>+7x<rsub|2>+3x<rsub|3>-x<rsub|4>=2>

      <math|-x<rsub|1>+4x<rsub|2>+9x<rsub|3>+2x<rsub|4>=1>

      <math|x<rsub|1>-x<rsub|2>+x<rsub|3>+4x<rsub|4>>=3
    </cell>>>>
  </wide-tabular>

  En este sistema se pedia obtener una solución partiendo el vector inicial 0
  y una toleracia variable, en este caso obtamos por una tolerancia
  <math|\<varepsilon\>=0.1> y sabiendo que los resultados eran
  <math|x<rsub|1>=2.7273;x<rsub|2>=-0.4040;x<rsub|3>=0.6364:x<rsub|4>=-0.1919>.
  Obtuvimos los resultados recogidos en la siguiente tabla

  \;

  <\big-table|<tabular|<tformat|<table|<row|<cell|<tabular|<tformat|<cwith|2|4|1|1|cell-valign|c>|<cwith|2|4|1|1|cell-halign|c>|<cwith|2|4|1|1|cell-lborder|1ln>|<cwith|2|2|1|1|cell-hyphen|n>|<cwith|2|2|1|1|cell-lborder|1ln>|<cwith|2|4|2|2|cell-lborder|1ln>|<cwith|2|4|1|1|cell-rborder|1ln>|<cwith|2|4|2|2|cell-rborder|1ln>|<cwith|2|4|3|3|cell-lborder|1ln>|<cwith|2|4|3|3|cell-rborder|1ln>|<cwith|1|1|1|4|cell-tborder|1ln>|<cwith|1|1|1|4|cell-bborder|1ln>|<cwith|2|2|1|4|cell-tborder|1ln>|<cwith|1|1|1|1|cell-lborder|1ln>|<cwith|1|1|2|4|cell-tborder|1ln>|<cwith|1|1|2|4|cell-bborder|1ln>|<cwith|2|2|2|4|cell-tborder|1ln>|<cwith|1|1|2|2|cell-lborder|1ln>|<cwith|1|1|1|1|cell-rborder|1ln>|<cwith|1|1|3|3|cell-tborder|1ln>|<cwith|1|1|3|3|cell-bborder|1ln>|<cwith|2|2|3|3|cell-tborder|1ln>|<cwith|1|1|3|3|cell-rborder|1ln>|<cwith|1|1|2|2|cell-rborder|1ln>|<cwith|1|1|3|3|cell-lborder|1ln>|<cwith|1|4|2|4|cell-background|>|<cwith|1|4|2|4|cell-halign|c>|<cwith|3|3|1|-1|cell-tborder|1ln>|<cwith|2|2|1|-1|cell-bborder|1ln>|<cwith|3|3|1|-1|cell-bborder|1ln>|<cwith|3|3|1|1|cell-lborder|1ln>|<cwith|3|3|3|3|cell-rborder|1ln>|<table|<row|<cell|iteración>|<cell|<math|x<rsup|1>>>|<cell|<math|<rsup|>>Final>>|<row|<cell|Gauss-Seidel>|<cell|[
  2.4 \ -0.057 \ 0.4031 \ \ 0.0349]>|<cell|<math|x<rsup|4>=>[ 2.6533 -0.3441
  \ 0.5841 -0.1453]>>|<row|<cell|Jacobi>|<cell|[2.4 \ 0.2857 0.1111 0.75
  ]>|<cell|<math|x<rsup|5>=>[ 2.5183 -0.2006 \ 0.4362 \ 0.0148 ]>>>>>>>>>>>
    \;
  </big-table>

  Con estos dos ejemplos ya se puede observar que el metodo de Gauss-Seidel
  converge más rapido que el de Jacobi. Además dicha convergencia se da en
  numeros más cercanos a la solución real. Para hacerlo más evidente vamos a
  ver 4 tablas más con los resultados arrojados al imponer un
  <math|\<varepsilon\><rsub|1>=0.01,\<varepsilon\><rsub|2>=0.001>

  <\big-table|<tabular|<tformat|<table|<row|<cell|<tabular|<tformat|<cwith|3|5|1|1|cell-valign|c>|<cwith|3|5|1|1|cell-halign|c>|<cwith|3|5|1|1|cell-lborder|1ln>|<cwith|3|3|1|1|cell-hyphen|n>|<cwith|3|3|1|1|cell-lborder|1ln>|<cwith|3|5|1|1|cell-rborder|1ln>|<cwith|3|5|2|2|cell-lborder|1ln>|<cwith|3|5|2|2|cell-rborder|1ln>|<cwith|2|2|1|3|cell-tborder|1ln>|<cwith|2|2|1|3|cell-bborder|1ln>|<cwith|3|3|1|3|cell-tborder|1ln>|<cwith|2|2|1|1|cell-lborder|1ln>|<cwith|2|2|2|3|cell-tborder|1ln>|<cwith|2|2|2|3|cell-bborder|1ln>|<cwith|3|3|2|3|cell-tborder|1ln>|<cwith|2|2|1|1|cell-rborder|1ln>|<cwith|2|2|2|2|cell-tborder|1ln>|<cwith|2|2|2|2|cell-bborder|1ln>|<cwith|3|3|2|2|cell-tborder|1ln>|<cwith|2|2|2|2|cell-rborder|1ln>|<cwith|2|2|2|2|cell-lborder|1ln>|<cwith|2|5|2|3|cell-background|>|<cwith|2|5|2|3|cell-halign|c>|<cwith|4|4|1|-1|cell-tborder|1ln>|<cwith|3|3|1|-1|cell-bborder|1ln>|<cwith|4|4|1|-1|cell-bborder|1ln>|<cwith|4|4|1|1|cell-lborder|1ln>|<cwith|4|4|2|2|cell-rborder|1ln>|<cwith|1|1|1|1|cell-row-span|1>|<cwith|1|1|1|1|cell-col-span|4>|<cwith|1|1|1|1|cell-valign|c>|<cwith|1|1|1|1|cell-halign|c>|<table|<row|<cell|
  Ejercicio 1(<math|\<varepsilon\><rsub|1>>)>|<cell|>>|<row|<cell|>|<cell|<math|<rsup|>>Final>>|<row|<cell|Gauss-Seidel>|<cell|<math|x<rsup|3>=>[
  3.00003 \ -2.4999 \ 6.99999]>>|<row|<cell|Jacobi>|<cell|<math|x<rsup|4>=>[
  3.00002 \ -2.500002 \ 6.99998]>>>>>>>>>>>
    \;
  </big-table>

  <\big-table|<tabular|<tformat|<table|<row|<cell|<tabular|<tformat|<cwith|3|5|1|1|cell-valign|c>|<cwith|3|5|1|1|cell-halign|c>|<cwith|3|5|1|1|cell-lborder|1ln>|<cwith|3|3|1|1|cell-hyphen|n>|<cwith|3|3|1|1|cell-lborder|1ln>|<cwith|3|5|1|1|cell-rborder|1ln>|<cwith|3|5|2|2|cell-lborder|1ln>|<cwith|3|5|2|2|cell-rborder|1ln>|<cwith|2|2|1|3|cell-tborder|1ln>|<cwith|2|2|1|3|cell-bborder|1ln>|<cwith|3|3|1|3|cell-tborder|1ln>|<cwith|2|2|1|1|cell-lborder|1ln>|<cwith|2|2|2|3|cell-tborder|1ln>|<cwith|2|2|2|3|cell-bborder|1ln>|<cwith|3|3|2|3|cell-tborder|1ln>|<cwith|2|2|1|1|cell-rborder|1ln>|<cwith|2|2|2|2|cell-tborder|1ln>|<cwith|2|2|2|2|cell-bborder|1ln>|<cwith|3|3|2|2|cell-tborder|1ln>|<cwith|2|2|2|2|cell-rborder|1ln>|<cwith|2|2|2|2|cell-lborder|1ln>|<cwith|2|5|2|3|cell-background|>|<cwith|2|5|2|3|cell-halign|c>|<cwith|4|4|1|-1|cell-tborder|1ln>|<cwith|3|3|1|-1|cell-bborder|1ln>|<cwith|4|4|1|-1|cell-bborder|1ln>|<cwith|4|4|1|1|cell-lborder|1ln>|<cwith|4|4|2|2|cell-rborder|1ln>|<cwith|1|1|1|1|cell-row-span|1>|<cwith|1|1|1|1|cell-col-span|4>|<cwith|1|1|1|1|cell-valign|c>|<cwith|1|1|1|1|cell-halign|c>|<table|<row|<cell|
  Ejercicio 1(<math|\<varepsilon\><rsub|2>>)>|<cell|>>|<row|<cell|>|<cell|<math|<rsup|>>Final>>|<row|<cell|Gauss-Seidel>|<cell|<math|x<rsup|4>=>[
  3.0000003 -2.50000004 \ 6.99999]>>|<row|<cell|Jacobi>|<cell|<math|x<rsup|4>=>[
  3.00002 \ -2.500002 \ 6.99998]>>>>>>>>>>>
    \;
  </big-table>

  \;

  <\big-table|<tabular|<tformat|<table|<row|<cell|<tabular|<tformat|<cwith|3|5|1|1|cell-valign|c>|<cwith|3|5|1|1|cell-halign|c>|<cwith|3|5|1|1|cell-lborder|1ln>|<cwith|3|3|1|1|cell-hyphen|n>|<cwith|3|3|1|1|cell-lborder|1ln>|<cwith|3|5|1|1|cell-rborder|1ln>|<cwith|3|5|2|2|cell-lborder|1ln>|<cwith|3|5|2|2|cell-rborder|1ln>|<cwith|2|2|1|3|cell-tborder|1ln>|<cwith|2|2|1|3|cell-bborder|1ln>|<cwith|3|3|1|3|cell-tborder|1ln>|<cwith|2|2|1|1|cell-lborder|1ln>|<cwith|2|2|2|3|cell-tborder|1ln>|<cwith|2|2|2|3|cell-bborder|1ln>|<cwith|3|3|2|3|cell-tborder|1ln>|<cwith|2|2|1|1|cell-rborder|1ln>|<cwith|2|2|2|2|cell-tborder|1ln>|<cwith|2|2|2|2|cell-bborder|1ln>|<cwith|3|3|2|2|cell-tborder|1ln>|<cwith|2|2|2|2|cell-rborder|1ln>|<cwith|2|2|2|2|cell-lborder|1ln>|<cwith|2|5|2|3|cell-background|>|<cwith|2|5|2|3|cell-halign|c>|<cwith|4|4|1|-1|cell-tborder|1ln>|<cwith|3|3|1|-1|cell-bborder|1ln>|<cwith|4|4|1|-1|cell-bborder|1ln>|<cwith|4|4|1|1|cell-lborder|1ln>|<cwith|4|4|2|2|cell-rborder|1ln>|<cwith|1|1|1|1|cell-row-span|1>|<cwith|1|1|1|1|cell-col-span|2>|<cwith|1|1|1|1|cell-halign|c>|<table|<row|<cell|
  Ejercicio 2(<math|\<varepsilon\><rsub|1>>)>|<cell|>>|<row|<cell|iteración>|<cell|<math|<rsup|>>Final>>|<row|<cell|Gauss-Seidel>|<cell|<math|x<rsup|8>=>[
  2.7182 -0.3967 \ 0.6300 -0.1862]>>|<row|<cell|Jacobi>|<cell|<math|x<rsup|12>=>[
  2.6974 -0.3765 \ 0.6073 -0.1633]>>>>>>>>>>>
    \;
  </big-table>

  <\big-table|<tabular|<tformat|<table|<row|<cell|<tabular|<tformat|<cwith|3|5|1|1|cell-valign|c>|<cwith|3|5|1|1|cell-halign|c>|<cwith|3|5|1|1|cell-lborder|1ln>|<cwith|3|3|1|1|cell-hyphen|n>|<cwith|3|3|1|1|cell-lborder|1ln>|<cwith|3|5|1|1|cell-rborder|1ln>|<cwith|3|5|2|2|cell-lborder|1ln>|<cwith|3|5|2|2|cell-rborder|1ln>|<cwith|2|2|1|3|cell-tborder|1ln>|<cwith|2|2|1|3|cell-bborder|1ln>|<cwith|3|3|1|3|cell-tborder|1ln>|<cwith|2|2|1|1|cell-lborder|1ln>|<cwith|2|2|2|3|cell-tborder|1ln>|<cwith|2|2|2|3|cell-bborder|1ln>|<cwith|3|3|2|3|cell-tborder|1ln>|<cwith|2|2|1|1|cell-rborder|1ln>|<cwith|2|2|2|2|cell-tborder|1ln>|<cwith|2|2|2|2|cell-bborder|1ln>|<cwith|3|3|2|2|cell-tborder|1ln>|<cwith|2|2|2|2|cell-rborder|1ln>|<cwith|2|2|2|2|cell-lborder|1ln>|<cwith|2|5|2|3|cell-background|>|<cwith|2|5|2|3|cell-halign|c>|<cwith|4|4|1|-1|cell-tborder|1ln>|<cwith|3|3|1|-1|cell-bborder|1ln>|<cwith|4|4|1|-1|cell-bborder|1ln>|<cwith|4|4|1|1|cell-lborder|1ln>|<cwith|4|4|2|2|cell-rborder|1ln>|<cwith|1|1|1|1|cell-row-span|1>|<cwith|1|1|1|1|cell-col-span|2>|<twith|table-valign|c>|<cwith|1|1|1|1|cell-valign|c>|<cwith|1|1|1|1|cell-halign|c>|<table|<row|<cell|
  Ejercicio 2(<math|\<varepsilon\><rsub|2>>)>|<cell|>>|<row|<cell|>|<cell|<math|<rsup|>>Final>>|<row|<cell|Gauss-Seidel>|<cell|<math|x<rsup|12>=>[
  2.7261 -0.4031 \ 0.6355 -0.1912]>>|<row|<cell|Jacobi>|<cell|<math|x<rsup|21>=>[
  2.7248 -0.4018 \ 0.6340 -0.1896]>>>>>>>>>>>
    \;
  </big-table>

  Con lo que verificamos la tendencia que habiamos observado.

  \;
</body>

<\initial>
  <\collection>
    <associate|page-medium|paper>
  </collection>
</initial>

<\references>
  <\collection>
    <associate|auto-1|<tuple|1|1>>
    <associate|auto-10|<tuple|2|5>>
    <associate|auto-11|<tuple|3|5>>
    <associate|auto-12|<tuple|4|5>>
    <associate|auto-13|<tuple|5|5>>
    <associate|auto-14|<tuple|6|5>>
    <associate|auto-15|<tuple|7|6>>
    <associate|auto-2|<tuple|1.1|1>>
    <associate|auto-3|<tuple|1.2|1>>
    <associate|auto-4|<tuple|1|2>>
    <associate|auto-5|<tuple|2|2>>
    <associate|auto-6|<tuple|2.1|2>>
    <associate|auto-7|<tuple|1|3>>
    <associate|auto-8|<tuple|2|4>>
    <associate|auto-9|<tuple|2.2|4>>
  </collection>
</references>

<\auxiliary>
  <\collection>
    <\associate|table>
      <tuple|normal|<\surround|<hidden-binding|<tuple>|1>|>
        \;
      </surround>|<pageref|auto-4>>

      <tuple|normal|<\surround|<hidden-binding|<tuple>|2>|>
        \;
      </surround>|<pageref|auto-10>>

      <tuple|normal|<\surround|<hidden-binding|<tuple>|3>|>
        \;
      </surround>|<pageref|auto-11>>

      <tuple|normal|<\surround|<hidden-binding|<tuple>|4>|>
        \;
      </surround>|<pageref|auto-12>>

      <tuple|normal|<\surround|<hidden-binding|<tuple>|5>|>
        \;
      </surround>|<pageref|auto-13>>

      <tuple|normal|<\surround|<hidden-binding|<tuple>|6>|>
        \;
      </surround>|<pageref|auto-14>>

      <tuple|normal|<\surround|<hidden-binding|<tuple>|7>|>
        \;
      </surround>|<pageref|auto-15>>
    </associate>
    <\associate|toc>
      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|1<space|2spc>Raíces
      \ \ de \ \ funciones \ \ no \ \ lineales \ \ - \ \ Parte \ \ 3>
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-1><vspace|0.5fn>

      <with|par-left|<quote|1tab>|1.1<space|2spc>Presentacion de la
      covergencia del metodo Newton-Rapshon
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-2>>

      <with|par-left|<quote|1tab>|1.2<space|2spc>Convergencia para f(x) =
      <with|mode|<quote|math>|x<rsup|3>-3x+2> y
      <with|mode|<quote|math>|x<rsub|0>=-3>
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-3>>

      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|2<space|2spc>Resolución
      numérica de sistemas lineales> <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-5><vspace|0.5fn>

      <with|par-left|<quote|1tab>|2.1<space|2spc>Descripción e implementación
      de los algoritmos <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-6>>

      <with|par-left|<quote|4tab>|Gauss-Seidel
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-7><vspace|0.15fn>>

      <with|par-left|<quote|4tab>|Jacobi <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-8><vspace|0.15fn>>

      <with|par-left|<quote|1tab>|2.2<space|2spc>Problemas planteados y su
      resolución <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-9>>
    </associate>
  </collection>
</auxiliary>