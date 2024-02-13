import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";
import NavBar from "./components/nav-bar/NavBar";
import { Routes, Route } from "react-router-dom";
import Login from "./pages/login/Login";
import Tareas from "./pages/tareas/Tareas";
import Categorias from "./pages/categorias/Categorias";

function App() {
  const [count, setCount] = useState(0);

  return (
    <Routes>
      <Route path="/login" element={<Login />}></Route>

      <Route path="/categorias" element={<Tareas />}></Route>
      <Route path="/tareas" element={<Categorias />}></Route>

      <Route path="/*" element={<NavBar />}></Route>
    </Routes>
  );
}

export default App;
