// NavBar.js

import React from "react";
import { AppBar, Toolbar, Typography, Button } from "@mui/material";
import { useNavigate } from "react-router-dom";

const NavBar = () => {
  return (
    <AppBar position="static">
      <Toolbar>
        <Typography
          variant="h6"
          onClick={() => {
            navigate("/*");
          }}
          style={{ textDecoration: "none", color: "inherit" }}
        >
          My App
        </Typography>
        <Button
          onClick={() => {
            navigate("/login");
          }}
          color="inherit"
        >
          Login
        </Button>
        <Button
          onClick={() => {
            navigate("/categorias");
          }}
          color="inherit"
        >
          Categorias
        </Button>
        <Button
          onClick={() => {
            navigate("/tareas");
          }}
          color="inherit"
        >
          Tareas
        </Button>
      </Toolbar>
    </AppBar>
  );
};

export default NavBar;
