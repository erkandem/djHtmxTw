# Full-stack Django with HTMX and Tailwind

## Part 1

### C1 - Intro

A **cheaper** alternative to full-blown React FE & Django BE 
 - HTMX & Alpine.js (JQuery?)
 - Tailwind (utility classes)

#### HTMX

##### PRO
  - 12 KB minified zipped bundle
    - 31 kb minified zipped Jquery
  - SSR
    - e.g jquery would be entirely client side
  - "easy to learn"? less JS like?
    - declarative vs imperative in JQuery
  - enable anything to trigger XHR
    - hx-get, `hx-<method>`
    - would require event listener

##### CON
 - new (community, market)
 - no replacement for react 

##### Example:

```html
<div id="parent-div">
   <button hx-post="/clicked"
       hx-trigger="click"
       hx-target="#parent-div"
       hx-swap="outerHTML"
   >
       Click Me!
   </button>
</div>

```

Usage:
 - HTMX attrs prefixed with `hx`
 - `hx-trigger`: event
 - `hx-post`: xhr, method, and route
 - `hx-target` & `hx-swap` replaces parent-div with response
    - expects HTML response (?) instead of JSON

Ref: 
 - HTMX Project https://htmx.org/


#### Tailwind

##### PRO

 - "utility" css; parameterized classes
 - mobile first
 - much narrower style scoping compared to `card`
 - generic, easy to learn: base class + parameter type & range
 - IDE integration

 ##### CON
 - tight coupling with HTML
 - verbose since additive
 - no components like in e.g. bootstrap
 - harder to learn

##### example

```html
<div class="my-4 mx-auto text-sm lg:text-2xl text-slate-700">
  Tailwind CSS is a utility-first CSS framework.
</div>
```

 - `my`
   - margin-top: 1rem; /* 16px */
   - margin-bottom: 1rem; /* 16px */
 - `mx` margin right & left, param `auto`
   - margin-left: auto;
   - margin-right: auto;
 - `text-sm`
    - font-size: 0.875rem; /* 14px */
    - line-height: 1.25rem; /* 20px */
 - `lg:text-2xl`
   - on `@media (min-width: 1024px)`
     - font-size: 1.5rem; /* 24px */
     - line-height: 2rem; /* 32px */

 - `text-slate-700`
   - color: rgb(148 163 184);
traditional:

```html

<style>
    .custom-class {
        margin: 1rem auto;
        font-size: 0.875rem;
        color: #334155; 
    }

    @media (min-width: 1024px) {
        .custom-class {
            font-size: 1.5rem;
        }
    }

</style>
<div class="custom-class">
    Tailwind CSS is a utility-first CSS framework.
</div>
```

Ref: 
 - Tailwind Project: 

#### Alpine.js - "jQuery for the modern web"

##### Pro

 - 17 kb
 - close to Vue and Angular
 - sprinkled in HTML like JQuery

##### Con
 - more like JS vs HTMX
 - data needs to be transformed to gusto of alpine
 - paid comp lib


```html
<div x-data="{ count: 0 }">
  <span x-text="count"></span>
  <button x-on:click="count++">Increment</button>
</div>
```

 - `x-data` initial 
 - `x-text` bind the data to the value of `count` 
 - `x-on:click` event listener type click with increment directive `count++`

Ref:
 - https://alpinejs.dev/

#### Outline

 -  Part 1 - setup
   - setup django, how to integrate htmx, tailwind, alpine

 - Part 2 - usage
   - HTMX
     - click to edit
     - inline validation
     - Table
       - add
       - edit
       - remove
     - bulk update
     - search & filter 
     - infinite scroll
   - Tailwind usage
   - extend htmx with Alpine
     - Tooltip
     - select all
     - show data

  - Part 3 - prep for deployment
   - Allauth
   - Cypress
   - WhiteNoise
   - Gunicorn
   - Postgres
   - Docker & Compose
   - Heroku

#### Extra

check `examples/c1`

### C2 - Django Setup

 - Start the project after creating a virtualenv

```shell
pip install uv
make compile_local
make install_local
django-admin startproject core .
django-admin startapp party
```

 - create a custom user and connect it to the admin

