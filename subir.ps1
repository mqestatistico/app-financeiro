# Script para automatizar o envio ao Git
Write-Host "--- Iniciando processo de Deploy Local ---" -ForegroundColor Cyan

# 1. Adiciona alterações
git add .

# 2. Pede um comentário para o commit
$mensagem = Read-Host "Digite a descrição da alteração"
if (-not $mensagem) { $mensagem = "Ajustes automáticos $(Get-Date -Format 'dd/MM/yyyy HH:mm')" }

# 3. Commit
git commit -m "$mensagem"

# 4. Push (assumindo que o remote 'origin' e o branch 'main' estarão configurados)
Write-Host "Enviando para o repositório remoto..." -ForegroundColor Yellow
git push origin main

Write-Host "--- Concluído com sucesso! ---" -ForegroundColor Green