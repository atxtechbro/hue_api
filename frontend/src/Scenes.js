import React, { useState } from 'react';
import Button from '@mui/material/Button';
import Stack from '@mui/material/Stack';
import Box from '@mui/material/Box';
import { buttonStyle } from './styles';

function Scenes() {
  const apiHost = process.env.REACT_APP_API_HOST; // Reminder: Add error handling if apiHost is undefined

  const triggerScene = (url) => {
    fetch(`http://${apiHost}:5000${url}`)
      .then(response => response.text())
      .then(data => alert(data))
      .catch(error => console.error('Error:', error));
  };

  const [startTime, setStartTime] = useState("06:00");
  const [endTime, setEndTime] = useState("18:00");
  const [feedback, setFeedback] = useState(""); // State for user feedback

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch('/circadian_lighting', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ startTime, endTime }),
    })
    .then(response => response.json())
    .then(data => {
      setFeedback("Circadian lighting settings updated successfully.");
    })
    .catch(error => {
      console.error('Error:', error);
      setFeedback("Failed to update circadian lighting settings.");
    });
  };

  return (
    <Box 
      display="flex" 
      justifyContent="center" 
      alignItems="center" 
      height="calc(100vh - 60px)"
    
