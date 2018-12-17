##general

```printf("%d \n");```

%d for decimals, %f for floats, %s for strings, %c for chars

if you dont put "\n" then your buffer will not be flushed. seg faults will not be known.

seg fault means accessing the memo that you are not supposed to. check index out of range errors.

use valgrind ...code... to keep track of memo.



```*ptr```.

```&adr```.

```type *var = malloc (int * sizeof(type))``` doesnt 0 out the allocated place. raw memo
```type *var = calloc (int , sizeoftype)``` slower than malloc because 0ing.
```var=realloc(var, newsize * sizeof(type);```

```memset(ptr, replacing, sizeof(type))``` replaces the spaces with 'replacing' elem


to pass elem to func

for ints etc use ```&var``` as IN. then ```*var``` to respective place at top param and use as ```var``` in block. arrays go as it is. bu * to param.

pass by value copies, pass by ref uses pointers.

C destroys all inside vars in the func.

but if you malloc etc use free or it will stay in the heap unreachable :(


structs. define somewhere call later.

##snipetts


###if you want to increment array size:

```
struct sortCOO *listRes=NULL;malloc(0* sizeof(struct sortCOO)) //should be NULL and this. IDK WHY???

listRes=realloc(listRes, (finalNZ+1) * sizeof(struct sortCOO)); //then realloced

/*code assign etc*/

++finalNZ //inc if you need.
```

otherwise stack smash......



###if you want to sort sth:


you have to write your comparator function...

```
int comparatorFunction(const void *i, const void *j) {//const void *i etc should be must.
	int ii;
	int jj;

	ii = ((struct sortCOO *)i)->ij;//type conversion
	jj = ((struct sortCOO *)j)->ij;

	//printf("test %d %d \n",ii,jj);
	return ii - jj;//-1 for i < j, 0 for i==j, 1 for i>j
}

//qsort func
	qsort(arr, size, sizeof(type), comparatorFunction);
```
basically qsort gets those vars, and then for each element in the array (regardless of the type) compares them. the programmer's aim is to write func to convert type of desired to do the actual comparison. pretty cool as it gives you the independence.


###func declaration:

if you:
```
int foo(const void *param1, const void *param2){
/*code */
return 
}
```
you have to return sth or void* it.

then to top you have to define it.

```int foo(const void *param1, const void *param2);```

###

