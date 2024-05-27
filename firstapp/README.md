1. For creating the new app from scratch we can use:
```bash
npx create-vite your-project-name --template react 
```
- IF PROBLEM (npm uninstall -g create-react-app && install)

2. Create routers
```bash
npm i react-router-dom@latest
```

```javascript
import { BrowserRouter } from 'react-router-dom'
import { Routes, Route, Link, useLocation } from 'react-router-dom'

// Link  ->  works just like the anchor tag 
// <a href='...'>  ===  <Link to="..." />

function App() {
    return (
        <BrowserRouter>
            <Routes location={location} key={location.pathname}>
                <Route path='/' element={<Layout/>}>
                    <Route index element={<LandingPage/>} />
                    <Route path="/about" element={<About/>} />
                    <Route path="*" element={<Page404 />} />
                </Route>
            </Routes>
        </BrowserRouter>
    )
}
```


3. Create all other components that are required for your project
