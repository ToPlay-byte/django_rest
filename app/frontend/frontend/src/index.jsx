import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { createRoot } from 'react-dom/client'


console.log('hfsfasdfasddfdf') 
const root = document.getElementById('root')

const container = createRoot(root)
 
const router = createBrowserRouter([
    { 
        path: '/shop/', 
        element: <div>something</div>     
    }      
]) 
  
container.render( 
    <RouterProvider router={router} />
)