import { axios } from '../utils/axios'

export async function getTodos() {
  return axios.get('/todos')
}
