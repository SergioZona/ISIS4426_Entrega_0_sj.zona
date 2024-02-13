// Login.js

import React, { useState } from "react";
import { Button, Snackbar, TextField, Typography } from "@mui/material";
import { Alert } from "@mui/material";
import { useNavigate } from "react-router-dom";

const Login = () => {
  const navigate = useNavigate();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [openSnackbar, setOpenSnackbar] = useState(false);

  const handleUsernameChange = (event) => {
    setUsername(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  const handleLogin = async () => {
    try {
      const response = await fetch(
        "http://localhost:5000/usuarios/iniciar-sesion",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ username, password }),
        }
      );
      if (response.ok) {
        // Redirect to categories on successful login
        navigate("/categorias");
      } else {
        // Handle error response
        const data = await response.json();
        setError(data.message);
        setOpenSnackbar(true);
      }
    } catch (error) {
      console.error("Error logging in:", error);
      setError("An unexpected error occurred. Please try again later.");
      setOpenSnackbar(true);
    }
  };

  const handleSignUp = () => {
    navigate("/signup");
  };

  const handleCloseSnackbar = () => {
    setOpenSnackbar(false);
  };

  return (
    <div style={{ color: "black" }}>
      <Typography variant="h2">Login</Typography>
      <form>
        <TextField
          label="Username"
          variant="outlined"
          fullWidth
          margin="normal"
          value={username}
          onChange={handleUsernameChange}
        />
        <TextField
          label="Password"
          type="password"
          variant="outlined"
          fullWidth
          margin="normal"
          value={password}
          onChange={handlePasswordChange}
        />
        <Button variant="contained" color="primary" onClick={handleLogin}>
          Log In
        </Button>
        <Typography
          style={{ textDecoration: "underline", cursor: "pointer" }}
          onClick={handleSignUp}
        >
          Sign Up
        </Typography>
      </form>
      <Snackbar
        open={openSnackbar}
        autoHideDuration={6000}
        onClose={handleCloseSnackbar}
      >
        <Alert
          onClose={handleCloseSnackbar}
          severity="error"
          sx={{ width: "100%" }}
        >
          {error}
        </Alert>
      </Snackbar>
    </div>
  );
};

export default Login;
