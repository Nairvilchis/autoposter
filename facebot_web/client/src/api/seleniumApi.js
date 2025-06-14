const API_BASE_URL = 'http://localhost:5000'; // Reemplaza con la URL de tu API de Flask

export const navigate = async (url) => {
  try {
    const response = await fetch(`${API_BASE_URL}/navigate`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ url }),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
// hhas 
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error al navegar:', error);
    throw error;
  }
};