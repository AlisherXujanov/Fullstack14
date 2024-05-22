/* eslint-disable react-refresh/only-export-components */
import { memo } from 'react' 

// API  ->  Application Programming Interface
// methods  =>  
//        GET    =>  Запрос на получение данных
//        POST   =>  Запрос на создание данных
//        PUT    =>  Запрос на обновление данных
//        PATCH  =>  Запрос на частичное обновление данных
//        DELETE =>  Запрос на удаление данных
// -------------------------------------------------------
// Promise  =>  обещание
//     3 состояния:
//        1. resolved  =>  выполнено
//        2. rejected  =>  отклонено
//        3. pending   =>  ожидание
// -------------------------------------------------------
// let data = {
//     name: "John",
//     age: 30
// };
// fetch   ->  
//     1.  fetch(url)  ->  отправляет GET запрос на сервер
//          if resolved  ->  если запрос выполнен успешно то ПОЛУЧАЕМ данных
//          if rejected  ->  если запрос выполнен с ошибкой то ПОЛУЧАЕМ ошибку
//     2.  fetch(url, {method:'POST',  body:JSON.stringify(data)})  ->  отправляет POST запрос на сервер
//          --------------------------------------------------
//          EXAMPLE with JSON:
//          let x = {...}
//          json  =>  JSON.stringify(x)  =>  "{}"
//          json  =>  JSON.parse("{}")    =>  {}
// -------------------------------------------------------
// HOMEWORK:
//  1. Learn about PROMISEs      =>  https://learn.javascript.ru/promise
//  2. Learn about fetch         =>  https://learn.javascript.ru/fetch
//  3. Learn about async/await   =>  https://learn.javascript.ru/async-await
//  4. JSON  stringify/parse     =>  https://learn.javascript.ru/json

// RU:
//  1. Изучить про PROMISEs     
//  2. Изучить про fetch        
//  3. Изучить про async/await   
//  4. JSON  stringify/parse     
// -------------------------------------------------------

function Test() {
    console.log("Компонент Test заново создан");
    return (
        <>
            <h1>Test</h1>        
            <p>lorem 1000</p>
        </>
    );
}

export default memo(Test);