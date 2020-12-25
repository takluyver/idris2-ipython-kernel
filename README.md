# Idris2 REPL Kernel
A simple IPython wrapper for the Idris2 REPL. Runs notebook commands through an Idris2 REPL process.

Make sure the path to the `idris2` executable is in your `path` environment variable.

## Install
From a shell running in the base of this project, run
```shell
jupyter kernelspec install idris2kernel
```

## Examples
```shell
:let plus2 : Nat -> Nat
:let plus2 n = n + 2
plus2 5
```
> `7`

```shell
:t [1..6]
```
> `rangeFromTo (fromInteger 1) (fromInteger 6) : List Integer`

## Todo
There's a lot missing. Since everything is run through the REPL, declaring functions with multiple lines is difficult, and you won't be able to `:exec` with variables defined by `:let`. 

* Look more into how IHaskell is built and model this off of that.